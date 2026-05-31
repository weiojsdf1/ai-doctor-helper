from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import SUPPORTED_IMAGE_EXTENSIONS, SUPPORTED_REPORT_EXTENSIONS
from app.models.file_record import FileRecord
from app.models.patient import Patient
from app.models.report_record import ReportRecord


def _safe_filename(filename: str) -> str:
    name = Path(filename).name
    return name.replace(" ", "_")


def _validate_extension(filename: str, allowed_extensions: set[str]) -> None:
    ext = Path(filename).suffix.lower()
    if ext not in allowed_extensions:
        allowed = ", ".join(sorted(allowed_extensions))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file extension '{ext}'. Allowed extensions: {allowed}",
        )


def save_upload_file(upload_file: UploadFile, destination_dir: Path) -> tuple[str, Path]:
    destination_dir.mkdir(parents=True, exist_ok=True)

    safe_name = _safe_filename(upload_file.filename or "uploaded_file")
    stored_filename = f"{uuid4().hex}_{safe_name}"
    destination_path = destination_dir / stored_filename

    with open(destination_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return stored_filename, destination_path


def save_patient_file(
    db: Session,
    patient: Patient,
    upload_file: UploadFile,
    file_type: str,
) -> FileRecord:
    if file_type not in {"xray", "lab", "other"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="file_type must be one of: xray, lab, other",
        )

    if file_type in {"xray", "lab"}:
        _validate_extension(upload_file.filename or "", SUPPORTED_IMAGE_EXTENSIONS)

    folder_name = "xrays" if file_type == "xray" else "labs" if file_type == "lab" else "other"
    destination_dir = Path(patient.patient_folder) / folder_name

    stored_filename, destination_path = save_upload_file(upload_file, destination_dir)

    record = FileRecord(
        patient_db_id=patient.id,
        file_type=file_type,
        original_filename=upload_file.filename or stored_filename,
        stored_filename=stored_filename,
        file_path=str(destination_path),
        content_type=upload_file.content_type,
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def save_patient_report(
    db: Session,
    patient: Patient,
    upload_file: UploadFile,
    report_type: str = "medical_report",
) -> ReportRecord:
    _validate_extension(upload_file.filename or "", SUPPORTED_REPORT_EXTENSIONS)

    destination_dir = Path(patient.patient_folder) / "reports"
    stored_filename, destination_path = save_upload_file(upload_file, destination_dir)

    record = ReportRecord(
        patient_db_id=patient.id,
        report_type=report_type,
        filename=stored_filename,
        file_path=str(destination_path),
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def ensure_existing_file(path: str) -> Path:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File was not found on disk.",
        )
    return file_path
