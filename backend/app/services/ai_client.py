from __future__ import annotations

import json
import os
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import requests
from sqlalchemy.orm import Session

import app.core.config as config
from app.models.chat_message import ChatMessage
from app.models.file_record import FileRecord
from app.models.patient import Patient
from app.models.report_record import ReportRecord
from app.services.cache_service import build_case_hash, load_cache, save_cache
from app.services.ai_config_service import get_effective_ai_service_url
from app.services.context_service import (
    build_patient_context_text,
    load_patient_context,
    local_context_answer,
    patient_to_dict,
    save_patient_context,
)
from app.services.report_builder import build_patient_report_html, default_report_filename


def _safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _safe_utc_datetime(value: Any) -> Optional[datetime]:
    if not value:
        return None
    try:
        text = str(value).strip().replace("Z", "")
        return datetime.fromisoformat(text)
    except Exception:
        return None


def _ai_service_url() -> str:
    # Dynamic URL has priority, so Kaggle/Cloudflare can update the backend
    # without restarting it. Environment AI_SERVICE_URL remains a backup.
    return get_effective_ai_service_url().rstrip("/")


def _ai_chat_mode() -> str:
    return str(getattr(config, "AI_CHAT_MODE", "") or os.getenv("AI_CHAT_MODE", "auto")).lower().strip()


def _request_timeout_seconds() -> int:
    configured = getattr(config, "AI_REQUEST_TIMEOUT_SECONDS", None) or os.getenv("AI_REQUEST_TIMEOUT_SECONDS")
    return max(10, _safe_int(configured, 900))


def _chat_timeout_seconds() -> int:
    configured = os.getenv("AI_CHAT_TIMEOUT_SECONDS", getattr(config, "AI_CHAT_TIMEOUT_SECONDS", None))
    return max(10, min(_safe_int(configured, 30), _request_timeout_seconds()))


class AIClient:
    def _patient_files(self, db: Session, patient: Patient) -> tuple[list[FileRecord], list[FileRecord]]:
        xrays = (
            db.query(FileRecord)
            .filter(FileRecord.patient_db_id == patient.id, FileRecord.file_type == "xray")
            .order_by(FileRecord.uploaded_at.desc())
            .all()
        )
        labs = (
            db.query(FileRecord)
            .filter(FileRecord.patient_db_id == patient.id, FileRecord.file_type == "lab")
            .order_by(FileRecord.uploaded_at.desc())
            .all()
        )
        return xrays, labs

    def _fallback_xray_result(self, image_path: Optional[str], reason: str) -> Dict[str, Any]:
        return {
            "image_path": image_path or "",
            "case_name": Path(image_path).name if image_path else "No X-ray image",
            "status": "fallback",
            "report": {
                "image_quality": "not assessed",
                "findings": "Live AI analysis was not completed.",
                "impression": reason,
                "abnormalities": [],
                "severity": "unknown",
                "recommendations": ["Review by a qualified physician/radiologist is recommended."],
                "patient_explanation": "The system could not complete live AI image analysis for this request.",
            },
            "alerts": [{"level": "warning", "message": "Live AI image analysis was unavailable or failed."}],
            "raw_output": "",
        }

    def _empty_lab_result(self, lab_path: Optional[str], message: str, status: str = "not_available") -> Dict[str, Any]:
        return {
            "image_path": lab_path or "",
            "status": status,
            "raw_text": "",
            "lab_data": {},
            "structured_values": {},
            "lab_context": message,
        }

    def _remote_post(
        self,
        endpoint: str,
        *,
        files: Dict[str, Any],
        data: Dict[str, str],
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        base_url = _ai_service_url()
        if not base_url:
            raise RuntimeError("AI_SERVICE_URL is not configured.")

        url = f"{base_url}/{endpoint.lstrip('/')}"
        response = requests.post(
            url,
            files=files,
            data=data,
            timeout=timeout or _request_timeout_seconds(),
            headers={"Connection": "close"},
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("status") != "success":
            raise RuntimeError(payload.get("message", "Remote AI service returned an error."))
        return payload

    def _remote_get_json(self, endpoint: str, *, timeout: Optional[int] = None) -> Dict[str, Any]:
        base_url = _ai_service_url()
        if not base_url:
            raise RuntimeError("AI_SERVICE_URL is not configured.")
        url = f"{base_url}/{endpoint.lstrip('/')}"
        response = requests.get(
            url,
            timeout=timeout or max(10, min(_chat_timeout_seconds(), 45)),
            headers={"Connection": "close"},
        )
        response.raise_for_status()
        payload = response.json()
        return payload if isinstance(payload, dict) else {}

    def _remote_post_json(self, endpoint: str, *, json_payload: Optional[Dict[str, Any]] = None, timeout: Optional[int] = None) -> Dict[str, Any]:
        base_url = _ai_service_url()
        if not base_url:
            raise RuntimeError("AI_SERVICE_URL is not configured.")
        url = f"{base_url}/{endpoint.lstrip('/')}"
        response = requests.post(
            url,
            json=json_payload or {},
            timeout=timeout or _request_timeout_seconds(),
            headers={"Connection": "close"},
        )
        response.raise_for_status()
        payload = response.json()
        return payload if isinstance(payload, dict) else {}

    def _prepare_lab_upload_file(self, lab_path: str) -> tuple[str, str, Optional[str]]:
        source = Path(lab_path)
        cleanup_path: Optional[str] = None

        try:
            from PIL import Image, ImageOps

            max_side = _safe_int(os.getenv("AI_LAB_UPLOAD_MAX_SIDE"), 1800)
            quality = _safe_int(os.getenv("AI_LAB_UPLOAD_JPEG_QUALITY"), 88)
            max_side = max(900, min(max_side, 2600))
            quality = max(60, min(quality, 95))

            with Image.open(source) as img:
                img = ImageOps.exif_transpose(img)
                width, height = img.size
                largest_side = max(width, height)
                if largest_side > max_side:
                    scale = max_side / float(largest_side)
                    new_size = (max(1, int(width * scale)), max(1, int(height * scale)))
                    img = img.resize(new_size)

                if img.mode not in {"RGB", "L"}:
                    img = img.convert("RGB")

                fd, temp_name = tempfile.mkstemp(prefix="ai_doctor_lab_upload_", suffix=".jpg")
                os.close(fd)
                img.save(temp_name, format="JPEG", quality=quality, optimize=True)
                cleanup_path = temp_name
                return temp_name, "image/jpeg", cleanup_path

        except Exception:
            return str(source), "application/octet-stream", cleanup_path

    def _has_meaningful_xray_result(self, xray_result: Any) -> bool:
        if not isinstance(xray_result, dict):
            return False

        status = str(xray_result.get("status", "")).lower().strip()
        if status in {"fallback", "failed", "error", "not_available"}:
            return False

        report = xray_result.get("report") or {}
        if not isinstance(report, dict):
            return False

        useful_fields = [
            report.get("findings"),
            report.get("impression"),
            report.get("abnormalities"),
            report.get("recommendations"),
        ]
        return any(bool(item) for item in useful_fields)

    def _fetch_saved_remote_xray_result(
        self,
        patient_id: str,
        xray_path: str,
        *,
        min_saved_at_utc: Optional[datetime] = None,
    ) -> Optional[Dict[str, Any]]:
        base_url = _ai_service_url()
        if not base_url or not patient_id:
            return None

        try:
            payload = self._remote_get_json(f"/results/xray/{patient_id}")
            if payload.get("status") not in {"success", "ok"}:
                return None

            saved_at = _safe_utc_datetime(payload.get("saved_at_utc"))
            if min_saved_at_utc is not None and saved_at is not None and saved_at < min_saved_at_utc:
                return None

            result = payload.get("xray_result")
            if not isinstance(result, dict):
                return None
            result["image_path"] = xray_path
            result.setdefault("recovered_from_remote_result_store", True)
            return result
        except Exception:
            return None

    def _poll_saved_remote_xray_result(
        self,
        patient_id: str,
        xray_path: str,
        *,
        min_saved_at_utc: Optional[datetime] = None,
    ) -> Optional[Dict[str, Any]]:
        polls = max(1, min(_safe_int(os.getenv("AI_XRAY_RESULT_POLLS"), 8), 15))
        interval = max(2, min(_safe_int(os.getenv("AI_XRAY_RESULT_POLL_SECONDS"), 4), 15))

        for _ in range(polls):
            result = self._fetch_saved_remote_xray_result(
                patient_id,
                xray_path,
                min_saved_at_utc=min_saved_at_utc,
            )
            if result is not None and self._has_meaningful_xray_result(result):
                return result
            time.sleep(interval)
        return None

    def _call_remote_analyze_xray(self, xray_path: str, patient_info: Dict[str, Any]) -> Dict[str, Any]:
        patient_id = str(patient_info.get("patient_id", "")).strip()
        started_at = datetime.utcnow() - timedelta(seconds=3)

        try:
            with open(xray_path, "rb") as f:
                payload = self._remote_post(
                    "/analyze-xray",
                    files={"xray_file": (Path(xray_path).name, f, "application/octet-stream")},
                    data={
                        "patient_id": patient_id,
                        "patient_info": json.dumps(patient_info, ensure_ascii=False),
                    },
                )
            result = payload.get("xray_result")
            if not isinstance(result, dict):
                raise RuntimeError("Remote AI service did not return a valid xray_result.")
            result["image_path"] = xray_path
            return result
        except Exception:
            # Important demo protection:
            # Sometimes Cloudflare closes the response while Kaggle has already completed
            # the analysis and saved it in /results/xray/{patient_id}. Recover it instead
            # of falling back to a weak local message.
            recovered = self._poll_saved_remote_xray_result(
                patient_id,
                xray_path,
                min_saved_at_utc=started_at,
            )
            if recovered is not None:
                return recovered
            raise

    def _fetch_saved_remote_lab_result(self, patient_id: str, lab_path: str) -> Optional[Dict[str, Any]]:
        base_url = _ai_service_url()
        if not base_url or not patient_id:
            return None

        url = f"{base_url}/results/lab/{patient_id}"
        try:
            response = requests.get(
                url,
                timeout=max(10, min(_chat_timeout_seconds(), 45)),
                headers={"Connection": "close"},
            )
            if response.status_code == 404:
                return None
            response.raise_for_status()
            payload = response.json()
            if payload.get("status") not in {"success", "ok"}:
                return None
            result = payload.get("lab_result")
            if not isinstance(result, dict):
                return None
            result["image_path"] = lab_path
            result.setdefault("recovered_from_remote_result_store", True)
            return result
        except Exception:
            return None

    def _poll_saved_remote_lab_result(self, patient_id: str, lab_path: str) -> Optional[Dict[str, Any]]:
        polls = max(1, min(_safe_int(os.getenv("AI_LAB_RESULT_POLLS"), 6), 12))
        interval = max(2, min(_safe_int(os.getenv("AI_LAB_RESULT_POLL_SECONDS"), 5), 15))

        for _ in range(polls):
            result = self._fetch_saved_remote_lab_result(patient_id, lab_path)
            if result is not None:
                return result
            time.sleep(interval)
        return None

    def _call_remote_analyze_lab(self, lab_path: str, patient_info: Dict[str, Any]) -> Dict[str, Any]:
        last_error: Optional[Exception] = None
        attempts = max(1, min(_safe_int(os.getenv("AI_LAB_OCR_RETRIES"), 3), 5))
        patient_id = str(patient_info.get("patient_id", "")).strip()

        recovered = self._fetch_saved_remote_lab_result(patient_id, lab_path)
        if recovered is not None and self._has_meaningful_lab_result(recovered):
            return recovered

        for attempt in range(1, attempts + 1):
            upload_path = lab_path
            mime_type = "application/octet-stream"
            cleanup_path: Optional[str] = None

            try:
                upload_path, mime_type, cleanup_path = self._prepare_lab_upload_file(lab_path)

                with open(upload_path, "rb") as f:
                    payload = self._remote_post(
                        "/analyze-lab",
                        files={"lab_file": (Path(upload_path).name, f, mime_type)},
                        data={
                            "patient_id": patient_id,
                            "patient_info": json.dumps(patient_info, ensure_ascii=False),
                        },
                    )

                result = payload.get("lab_result")
                if not isinstance(result, dict):
                    raise RuntimeError("Remote AI service did not return a valid lab_result.")

                result["image_path"] = lab_path
                result.setdefault("upload_optimization", "compressed_lab_upload")
                return result

            except Exception as exc:
                last_error = exc
                recovered = self._poll_saved_remote_lab_result(patient_id, lab_path)
                if recovered is not None and self._has_meaningful_lab_result(recovered):
                    return recovered
                if attempt < attempts:
                    time.sleep(5 * attempt)

            finally:
                if cleanup_path:
                    try:
                        Path(cleanup_path).unlink(missing_ok=True)
                    except Exception:
                        pass

        raise RuntimeError(f"Remote lab OCR failed after {attempts} attempts: {last_error}")

    def _has_meaningful_lab_result(self, lab_result: Any) -> bool:
        if not isinstance(lab_result, dict):
            return False

        status = str(lab_result.get("status", "")).lower().strip()
        if status in {"fallback", "failed", "error", "not_available"}:
            return False

        lab_data = lab_result.get("lab_data") or {}
        structured_values = lab_result.get("structured_values") or {}
        raw_text = str(lab_result.get("raw_text") or "").strip()
        lab_context = str(lab_result.get("lab_context") or "").strip().lower()

        if lab_data or structured_values or raw_text:
            return True
        if status in {"success", "completed"} and lab_context and "unavailable" not in lab_context:
            return True
        return False

    def _cache_is_usable(self, cached: Any, xray_path: Optional[str], lab_path: Optional[str]) -> bool:
        if not isinstance(cached, dict):
            return False

        warnings = cached.get("warnings", []) or []
        warning_blob = " ".join(str(item).lower() for item in warnings)
        failure_markers = ["failed", "unavailable", "connection aborted", "remote disconnected", "not found", "internal server error"]
        if any(marker in warning_blob for marker in failure_markers):
            return False

        xray_result = cached.get("xray_result")
        if xray_path:
            if not isinstance(xray_result, dict):
                return False
            if str(xray_result.get("status", "")).lower() in {"fallback", "failed", "error"}:
                return False

        lab_result = cached.get("lab_result")
        if lab_path and not self._has_meaningful_lab_result(lab_result):
            return False

        return True

    def _load_json_file(self, path: Path) -> Optional[Any]:
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return None

    def _load_existing_xray_result(self, patient: Patient) -> Optional[Dict[str, Any]]:
        output_dir = Path(patient.patient_folder) / "outputs"
        data = self._load_json_file(output_dir / "xray_results.json")
        if isinstance(data, list) and data and isinstance(data[0], dict):
            return data[0]
        if isinstance(data, dict):
            return data
        context = load_patient_context(patient.patient_folder) or {}
        xray_result = context.get("xray_result")
        return xray_result if isinstance(xray_result, dict) else None

    def _load_existing_lab_result(self, patient: Patient) -> Optional[Dict[str, Any]]:
        output_dir = Path(patient.patient_folder) / "outputs"
        data = self._load_json_file(output_dir / "lab_ocr_result.json")
        if isinstance(data, dict):
            return data
        context = load_patient_context(patient.patient_folder) or {}
        lab_result = context.get("lab_result")
        return lab_result if isinstance(lab_result, dict) else None

    def _save_report_record(self, db: Session, patient: Patient, filename: str, html_text: str) -> ReportRecord:
        reports_dir = Path(patient.patient_folder) / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = reports_dir / filename
        report_path.write_text(html_text, encoding="utf-8")

        record = ReportRecord(
            patient_db_id=patient.id,
            report_type="medical_report",
            filename=filename,
            file_path=str(report_path),
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    def _save_case_state(
        self,
        db: Session,
        patient: Patient,
        patient_info: Dict[str, Any],
        xray_result: Dict[str, Any],
        lab_result: Dict[str, Any],
        warnings: list[str],
        source: str,
        cache_key: Optional[str],
        message: str,
        available_xray_files: int,
        available_lab_files: int,
    ) -> dict:
        output_dir = Path(patient.patient_folder) / "outputs"
        output_dir.mkdir(parents=True, exist_ok=True)

        (output_dir / "xray_results.json").write_text(json.dumps([xray_result], indent=2, ensure_ascii=False), encoding="utf-8")
        (output_dir / "lab_ocr_result.json").write_text(json.dumps(lab_result, indent=2, ensure_ascii=False), encoding="utf-8")

        context_text = build_patient_context_text(patient_info, xray_result, lab_result, warnings)
        context = {
            "patient_info": patient_info,
            "xray_result": xray_result,
            "lab_result": lab_result,
            "warnings": warnings,
            "source": source,
            "cache_key": cache_key,
            "context_text": context_text,
        }
        save_patient_context(patient.patient_folder, context)

        report_html = build_patient_report_html(
            patient_info=patient_info,
            xray_result=xray_result,
            lab_result=lab_result,
            warnings=warnings,
            source=source,
        )
        filename = default_report_filename(patient_info)
        report_record = self._save_report_record(db, patient, filename, report_html)

        return {
            "status": "success" if source in {"remote_ai", "cache", "partial_remote_ai", "xray_remote_ai", "xray_remote_ai_recovered", "lab_merged_remote_ai"} else "fallback",
            "message": message,
            "patient_id": patient.patient_id,
            "available_xray_files": available_xray_files,
            "available_lab_files": available_lab_files,
            "warnings": warnings,
            "source": source,
            "cache_key": cache_key,
            "report_id": report_record.id,
            "report_filename": report_record.filename,
            "report_download_url": f"/api/patients/{patient.patient_id}/reports/{report_record.id}/download",
        }

    def analyze_xray_only(self, db: Session, patient: Patient) -> dict:
        xrays, labs = self._patient_files(db, patient)
        warnings: list[str] = []
        patient_info = patient_to_dict(patient)
        selected_xray = xrays[0] if xrays else None
        xray_path = selected_xray.file_path if selected_xray else None

        if not xray_path:
            reason = "No Chest X-ray image was uploaded."
            warnings.append(reason)
            xray_result = self._fallback_xray_result(None, reason)
            source = "fallback"
        else:
            try:
                xray_result = self._call_remote_analyze_xray(xray_path, patient_info)
                source = "xray_remote_ai_recovered" if xray_result.get("recovered_from_remote_result_store") else "xray_remote_ai"
            except Exception as exc:
                reason = f"Remote X-ray analysis failed: {exc}"
                warnings.append(reason)
                xray_result = self._fallback_xray_result(xray_path, reason)
                source = "fallback"

        existing_lab = self._load_existing_lab_result(patient)
        lab_result = existing_lab if isinstance(existing_lab, dict) else self._empty_lab_result(
            None,
            "No lab report has been analyzed yet. Lab analysis is optional and can be added later.",
            status="not_provided",
        )

        cache_key = build_case_hash(xray_path, None)
        return self._save_case_state(
            db=db,
            patient=patient,
            patient_info=patient_info,
            xray_result=xray_result,
            lab_result=lab_result,
            warnings=warnings,
            source=source,
            cache_key=cache_key,
            message="X-ray analysis completed. Lab analysis can be added later.",
            available_xray_files=len(xrays),
            available_lab_files=len(labs),
        )

    def analyze_lab_and_merge(self, db: Session, patient: Patient) -> dict:
        xrays, labs = self._patient_files(db, patient)
        warnings: list[str] = []
        patient_info = patient_to_dict(patient)
        selected_lab = labs[0] if labs else None
        lab_path = selected_lab.file_path if selected_lab else None

        existing_xray = self._load_existing_xray_result(patient)
        if isinstance(existing_xray, dict):
            xray_result = existing_xray
        else:
            reason = "No saved X-ray analysis was found. Run X-ray analysis first for best integrated interpretation."
            warnings.append(reason)
            selected_xray = xrays[0] if xrays else None
            xray_result = self._fallback_xray_result(selected_xray.file_path if selected_xray else None, reason)

        if not lab_path:
            warning = "No lab report image was uploaded."
            warnings.append(warning)
            lab_result = self._empty_lab_result(None, warning, status="not_provided")
            source = "partial_remote_ai" if str(xray_result.get("status", "")).lower() not in {"fallback", "failed", "error"} else "fallback"
        else:
            try:
                lab_result = self._call_remote_analyze_lab(lab_path, patient_info)
                if self._has_meaningful_lab_result(lab_result):
                    source = "lab_merged_remote_ai"
                else:
                    warnings.append("Remote lab OCR completed but did not return usable extracted lab text or values.")
                    source = "partial_remote_ai"
            except Exception as exc:
                warnings.append(f"Remote lab OCR failed: {exc}")
                lab_result = self._empty_lab_result(
                    lab_path,
                    "Remote lab OCR was unavailable. The uploaded lab image is stored, and the X-ray analysis remains available.",
                    status="fallback",
                )
                source = "partial_remote_ai" if str(xray_result.get("status", "")).lower() not in {"fallback", "failed", "error"} else "fallback"

        cache_key = build_case_hash((xrays[0].file_path if xrays else None), lab_path)
        return self._save_case_state(
            db=db,
            patient=patient,
            patient_info=patient_info,
            xray_result=xray_result,
            lab_result=lab_result,
            warnings=warnings,
            source=source,
            cache_key=cache_key,
            message="Lab analysis and X-ray merge completed." if source == "lab_merged_remote_ai" else "Lab merge completed with warnings.",
            available_xray_files=len(xrays),
            available_lab_files=len(labs),
        )

    def analyze_patient(self, db: Session, patient: Patient) -> dict:
        xrays, labs = self._patient_files(db, patient)
        warnings: list[str] = []
        patient_info = patient_to_dict(patient)

        selected_xray = xrays[0] if xrays else None
        selected_lab = labs[0] if labs else None
        xray_path = selected_xray.file_path if selected_xray else None
        lab_path = selected_lab.file_path if selected_lab else None

        if not xray_path:
            warnings.append("No Chest X-ray image was uploaded. X-ray analysis was skipped.")
        if not lab_path:
            warnings.append("No lab report image was uploaded. Lab context is unavailable.")

        cache_key = build_case_hash(xray_path, lab_path)
        cached_payload = load_cache(cache_key)
        cached = cached_payload if self._cache_is_usable(cached_payload, xray_path, lab_path) else None

        if cached:
            xray_result = cached.get("xray_result")
            lab_result = cached.get("lab_result", {})
            warnings.extend(cached.get("warnings", []))
            source = "cache"
            message = "Analysis completed using cached results."
        else:
            xray_remote_ok = False
            lab_remote_ok = False

            if xray_path:
                try:
                    xray_result = self._call_remote_analyze_xray(xray_path, patient_info)
                    xray_remote_ok = True
                except Exception as exc:
                    reason = f"Remote X-ray analysis failed: {exc}"
                    warnings.append(reason)
                    xray_result = self._fallback_xray_result(xray_path, reason)
            else:
                xray_result = self._fallback_xray_result(None, "No X-ray image was uploaded.")

            if lab_path:
                try:
                    lab_result = self._call_remote_analyze_lab(lab_path, patient_info)
                    lab_remote_ok = self._has_meaningful_lab_result(lab_result)
                    if not lab_remote_ok:
                        warnings.append("Remote lab OCR completed but did not return usable extracted lab text or values.")
                except Exception as exc:
                    warnings.append(f"Remote lab OCR failed: {exc}")
                    lab_result = self._empty_lab_result(
                        lab_path,
                        "Remote lab OCR was unavailable. The uploaded lab image is stored but no structured values were extracted.",
                        status="fallback",
                    )
            else:
                lab_result = self._empty_lab_result(None, "No lab report image was uploaded.", status="not_provided")

            xray_requirement_ok = (not xray_path) or xray_remote_ok
            lab_requirement_ok = (not lab_path) or lab_remote_ok
            any_remote_ok = xray_remote_ok or lab_remote_ok

            if xray_requirement_ok and lab_requirement_ok and any_remote_ok:
                source = "remote_ai"
            elif any_remote_ok:
                source = "partial_remote_ai"
            else:
                source = "fallback"
            message = "Analysis completed."

            if source == "remote_ai":
                save_cache(
                    cache_key,
                    {
                        "xray_result": xray_result,
                        "lab_result": lab_result,
                        "warnings": warnings,
                        "source": source,
                        "cache_key": cache_key,
                    },
                )

        return self._save_case_state(
            db=db,
            patient=patient,
            patient_info=patient_info,
            xray_result=xray_result,
            lab_result=lab_result,
            warnings=warnings,
            source=source,
            cache_key=cache_key,
            message=message,
            available_xray_files=len(xrays),
            available_lab_files=len(labs),
        )

    def _local_answer_with_notice(self, context_text: str, question: str, context: Optional[Dict[str, Any]]) -> str:
        local_answer = local_context_answer(context_text, question, context=context)
        return (
            "Note: This response was generated locally from the saved report context because the remote AI service is not currently being used or is unavailable.\n\n"
            + local_answer
        )

    def _remote_chat_answer(self, context_text: str, question: str) -> str:
        base_url = _ai_service_url()
        if not base_url:
            raise RuntimeError("AI_SERVICE_URL is not configured.")

        last_error: Optional[Exception] = None
        attempts = max(1, min(_safe_int(os.getenv("AI_CHAT_RETRIES"), 2), 3))

        for attempt in range(1, attempts + 1):
            try:
                response = requests.post(
                    f"{base_url}/chat",
                    json={"context": context_text, "question": question},
                    timeout=_chat_timeout_seconds(),
                    headers={"Connection": "close"},
                )
                response.raise_for_status()
                payload = response.json()

                if payload.get("status") not in {None, "success"}:
                    raise RuntimeError(payload.get("message", "Remote chat returned an error."))

                answer = str(payload.get("answer", "")).strip()
                if not answer:
                    raise RuntimeError("Remote chat returned an empty answer.")

                return answer
            except Exception as exc:
                last_error = exc
                if attempt < attempts:
                    time.sleep(1.5 * attempt)

        raise RuntimeError(f"Remote chat failed after {attempts} attempts: {last_error}")

    def check_remote_service(self) -> Dict[str, Any]:
        base_url = _ai_service_url()
        if not base_url:
            return {"configured": False, "status": "not_configured", "message": "AI_SERVICE_URL is not configured."}
        try:
            payload = self._remote_get_json("/health", timeout=30)
            return {"configured": True, "status": "ok", "service_url": base_url, "remote": payload}
        except Exception as exc:
            return {"configured": True, "status": "unreachable", "service_url": base_url, "error": str(exc)}

    def warmup_remote_service(self) -> Dict[str, Any]:
        base_url = _ai_service_url()
        if not base_url:
            return {"configured": False, "status": "not_configured", "message": "AI_SERVICE_URL is not configured."}

        timeout = max(60, _safe_int(os.getenv("AI_WARMUP_TIMEOUT_SECONDS"), 900))
        try:
            payload = self._remote_post_json("/warmup", timeout=timeout)
            health = self.check_remote_service()
            return {"configured": True, "status": "ok", "service_url": base_url, "warmup": payload, "health": health}
        except Exception as exc:
            return {"configured": True, "status": "failed", "service_url": base_url, "error": str(exc)}

    def chat_with_patient_context(self, db: Session, patient: Patient, question: str) -> tuple[str, str]:
        user_msg = ChatMessage(patient_db_id=patient.id, role="user", content=question)
        db.add(user_msg)
        db.commit()

        context = load_patient_context(patient.patient_folder) or {}
        context_text = context.get("context_text", "")

        source = "local"
        remote_allowed = _ai_chat_mode() in {"auto", "remote"}

        if remote_allowed and _ai_service_url() and context_text:
            try:
                answer = self._remote_chat_answer(context_text, question)
                source = "remote_ai"
            except Exception:
                answer = self._local_answer_with_notice(context_text, question, context)
                source = "local_fallback"
        else:
            answer = self._local_answer_with_notice(context_text, question, context)
            source = "local"

        assistant_msg = ChatMessage(patient_db_id=patient.id, role="assistant", content=answer)
        db.add(assistant_msg)
        db.commit()

        return answer, source


ai_client = AIClient()
