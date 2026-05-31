from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.core.config import DISCLAIMER
from app.models.patient import Patient


def patient_to_dict(patient: Patient) -> Dict[str, Any]:
    return {
        "patient_name": patient.patient_name,
        "patient_id": patient.patient_id,
        "age": patient.age,
        "sex": patient.sex,
        "phone": patient.phone,
        "symptoms_or_notes": patient.symptoms_or_notes,
        "created_at": patient.created_at.isoformat() if patient.created_at else "",
    }


def _clean(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value).strip()


def _lab_values_text(lab_result: Dict[str, Any]) -> str:
    lab_data = lab_result.get("lab_data") or lab_result.get("structured_values") or {}
    if isinstance(lab_data, dict) and lab_data:
        rows = []
        for name, data in lab_data.items():
            if isinstance(data, dict):
                value = data.get("value", "")
                unit = data.get("unit", "")
                status = data.get("status", "unknown")
                rows.append(f"{name}: {value} {unit} ({status})".strip())
            else:
                rows.append(f"{name}: {data}".strip())
        if rows:
            return "; ".join(rows)

    raw_text = str(lab_result.get("raw_text") or "").strip()
    lab_context = str(lab_result.get("lab_context") or "").strip()

    if lab_context and raw_text:
        return f"{lab_context} Extracted OCR text: {raw_text[:1500]}"
    if lab_context:
        return lab_context
    if raw_text:
        return f"Extracted OCR text: {raw_text[:1500]}"

    return "No structured lab values available."


def build_patient_context_text(
    patient_info: Dict[str, Any],
    xray_result: Optional[Dict[str, Any]],
    lab_result: Optional[Dict[str, Any]],
    warnings: Optional[List[str]] = None,
) -> str:
    xray_result = xray_result or {}
    lab_result = lab_result or {}
    warnings = warnings or []
    report = xray_result.get("report", {}) or {}
    alerts = xray_result.get("alerts", []) or []

    return f"""
PATIENT INFORMATION
-------------------
{json.dumps(patient_info, indent=2, ensure_ascii=False)}

CHEST X-RAY AI REPORT
---------------------
Status: {xray_result.get('status', 'Not provided')}
Image quality: {_clean(report.get('image_quality', 'Not provided'))}
Severity: {_clean(report.get('severity', 'Not provided'))}
Findings: {_clean(report.get('findings', 'Not provided'))}
Impression: {_clean(report.get('impression', 'Not provided'))}
Abnormalities: {_clean(report.get('abnormalities', []))}
Recommendations: {_clean(report.get('recommendations', []))}
Patient explanation: {_clean(report.get('patient_explanation', 'Not provided'))}

ALERTS
------
{json.dumps(alerts, indent=2, ensure_ascii=False)}

LAB REPORT OCR
--------------
Status: {lab_result.get('status', 'not_available')}
Structured values: {_lab_values_text(lab_result)}
Lab interpretation: {lab_result.get('lab_context', 'No structured lab context available.')}

WARNINGS
--------
{json.dumps(warnings, indent=2, ensure_ascii=False)}

DISCLAIMER
----------
{DISCLAIMER}
""".strip()


def save_patient_context(patient_folder: str, context: Dict[str, Any]) -> Path:
    output_dir = Path(patient_folder) / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "patient_context.json"
    path.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")
    text_path = output_dir / "patient_context.txt"
    text_path.write_text(context.get("context_text", ""), encoding="utf-8")
    return path


def load_patient_context(patient_folder: str) -> Optional[Dict[str, Any]]:
    path = Path(patient_folder) / "outputs" / "patient_context.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _get_report(context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return (((context or {}).get("xray_result") or {}).get("report") or {})


def _get_alerts(context: Optional[Dict[str, Any]]) -> List[Any]:
    alerts = ((context or {}).get("xray_result") or {}).get("alerts") or []
    return alerts if isinstance(alerts, list) else [alerts]


def _get_lab_result(context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return ((context or {}).get("lab_result") or {})


def _sentence_join(items: List[str]) -> str:
    return " ".join(item.strip() for item in items if item and item.strip())


def _pneumonia_compatibility_text(report: Dict[str, Any], lab_result: Dict[str, Any]) -> str:
    findings_blob = " ".join([
        _clean(report.get("findings", "")),
        _clean(report.get("impression", "")),
        _clean(report.get("abnormalities", [])),
    ]).lower()
    lab_blob = _lab_values_text(lab_result).lower() + " " + str(lab_result.get("lab_context", "")).lower()

    imaging_support = any(term in findings_blob for term in ["opacity", "consolidation", "infiltrate", "pneumonia"])
    lab_support = any(term in lab_blob for term in ["wbc", "crp", "neutrophils", "esr", "high"])

    if imaging_support and lab_support:
        return (
            "The saved context includes X-ray findings such as opacity or consolidation, and the lab context includes abnormal inflammatory or infection-related markers. "
            "Together, these findings may be compatible with pneumonia or another inflammatory/infectious process, but they do not establish a final diagnosis. "
            "Clinical symptoms and physician/radiologist review are required."
        )
    if imaging_support:
        return (
            "The saved X-ray context includes opacity or possible consolidation. These imaging findings may be compatible with pneumonia in the right clinical setting, "
            "especially with symptoms such as fever, cough, or elevated inflammatory markers. The available information is not enough for a final diagnosis."
        )
    return (
        "The saved context does not clearly provide imaging findings that specifically support pneumonia. A physician or radiologist should review the image and clinical data."
    )


def local_context_answer(context_text: str, question: str, context: Optional[Dict[str, Any]] = None) -> str:
    q = question.lower().strip()
    if not context_text and not context:
        return "No analysis context is available yet. Please run analysis first."

    report = _get_report(context)
    lab_result = _get_lab_result(context)
    alerts = _get_alerts(context)
    warnings = (context or {}).get("warnings", []) or []

    findings = _clean(report.get("findings", ""))
    impression = _clean(report.get("impression", ""))
    abnormalities = _clean(report.get("abnormalities", []))
    severity = _clean(report.get("severity", ""))
    recommendations = _clean(report.get("recommendations", []))
    lab_values = _lab_values_text(lab_result)
    lab_context = _clean(lab_result.get("lab_context", ""))

    if any(term in q for term in ["final diagnosis", "diagnosis", "تشخيص"]):
        return (
            "No. This is not a final medical diagnosis. The answer is based only on the saved AI report and lab context. "
            "Final interpretation must be performed by a qualified physician or radiologist."
        )

    if any(term in q for term in ["pneumonia", "التهاب", "ذات الرئة"]):
        return _pneumonia_compatibility_text(report, lab_result)

    if any(term in q for term in ["consolidation", "opacity", "كثافة", "ارتشاح"]):
        return _sentence_join([
            f"The X-ray report describes: {findings}." if findings else "",
            f"The impression states: {impression}." if impression else "",
            "Opacity or consolidation can represent an air-space process and may be seen with infection, inflammation, atelectasis, or other causes. Clinical correlation is required.",
        ])

    if any(term in q for term in ["abnormal", "finding", "detected", "abnormality", "موجود", "شو"]):
        return _sentence_join([
            f"Detected X-ray findings: {findings}." if findings else "No specific X-ray findings are available in the saved context.",
            f"Listed abnormalities: {abnormalities}." if abnormalities else "",
            f"Severity: {severity}." if severity else "",
            f"Impression: {impression}." if impression else "",
            "These findings should be reviewed by a physician or radiologist.",
        ])

    if any(term in q for term in ["warning", "alert", "تنبيه", "تحذير"]):
        if alerts:
            alert_text = "; ".join(_clean(item) for item in alerts)
            return f"The saved alerts are: {alert_text}. Alerts are generated from severity, image quality, and important findings such as opacity, consolidation, effusion, pneumothorax, or cardiomegaly."
        return "No urgent alert is available in the saved context."

    if any(term in q for term in ["lab", "crp", "wbc", "neutrophil", "تحليل", "تحاليل"]):
        return _sentence_join([
            f"Extracted lab values: {lab_values}." if lab_values else "No structured lab values are available.",
            f"Lab interpretation: {lab_context}." if lab_context else "",
            "Lab results are supportive context only and must be interpreted with symptoms, examination, and imaging review.",
        ])

    if any(term in q for term in ["physician", "radiologist", "review", "doctor", "طبيب"]):
        return _sentence_join([
            "The physician or radiologist should review the original X-ray image, the reported findings and impression, image quality, and any alerts.",
            f"Recommendations from the report: {recommendations}." if recommendations else "",
            "Clinical symptoms and lab values should be correlated before any medical decision.",
        ])

    if any(term in q for term in ["differential", "causes", "سبب", "أسباب"]):
        return (
            "Based on a reported lung opacity or consolidation, possible considerations can include infection such as pneumonia, atelectasis, inflammatory change, fluid-related opacity, or less common structural causes. "
            "The saved AI report cannot determine the final cause without clinical correlation and radiologist review."
        )

    if any(term in q for term in ["explain", "simple", "summary", "summarize", "اشرح", "ملخص"]):
        return _sentence_join([
            f"Summary: the X-ray severity is {severity}." if severity else "Summary: the saved report is available.",
            f"Main X-ray finding: {findings}." if findings else "",
            f"Impression: {impression}." if impression else "",
            f"Lab context: {lab_context}." if lab_context else "",
            "This explanation is not a final diagnosis and should be reviewed by a qualified physician or radiologist.",
        ])

    if warnings:
        warning_text = "; ".join(str(w) for w in warnings)
    else:
        warning_text = "No major workflow warnings are saved."

    return _sentence_join([
        f"X-ray findings: {findings}." if findings else "The saved context does not include detailed X-ray findings.",
        f"Impression: {impression}." if impression else "",
        f"Lab context: {lab_context}." if lab_context else "",
        f"Workflow notes: {warning_text}",
        "Please ask about findings, pneumonia compatibility, lab relevance, alerts, or physician review for a more focused answer.",
    ])
