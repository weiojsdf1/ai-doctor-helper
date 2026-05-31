from __future__ import annotations

import base64
import html
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.core.config import DISCLAIMER


def _escape(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


def _display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _short_text(value: Any, limit: int = 900) -> str:
    text = str(value or "").strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + " ... [truncated]"


def _public_warning(value: Any) -> str:
    text = str(value or "").strip()
    lowered = text.lower()
    if "remote x-ray analysis failed" in lowered:
        return "Remote X-ray analysis was unavailable or interrupted. Please rerun the analysis or verify the AI service connection."
    if "remote lab ocr failed" in lowered:
        return "Remote lab extraction was unavailable or interrupted. Please verify the AI service connection and rerun lab analysis if needed."
    return text


def _image_data_uri(path: Optional[str]) -> str:
    if not path:
        return ""
    file_path = Path(path)
    if not file_path.exists():
        return ""
    ext = file_path.suffix.lower().replace(".", "") or "png"
    if ext == "jpg":
        ext = "jpeg"
    data = base64.b64encode(file_path.read_bytes()).decode("utf-8")
    return f"data:image/{ext};base64,{data}"


def _list_html(items: Any) -> str:
    if not items:
        return "<li>None</li>"
    if not isinstance(items, list):
        items = [items]
    return "".join(f"<li>{_escape(_display(item))}</li>" for item in items)


def _alerts_html(alerts: List[Dict[str, Any]]) -> str:
    if not alerts:
        return "<li>No alerts generated.</li>"
    rows = []
    for item in alerts:
        if isinstance(item, dict):
            rows.append(f"<li><strong>{_escape(item.get('level', 'alert'))}:</strong> {_escape(item.get('message', ''))}</li>")
        else:
            rows.append(f"<li>{_escape(item)}</li>")
    return "".join(rows)


def _normalise_lab_data(lab_result: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    lab_data = lab_result.get("lab_data") or lab_result.get("structured_values") or {}
    if not isinstance(lab_data, dict):
        return {}

    normalised: Dict[str, Dict[str, Any]] = {}
    for test_name, data in lab_data.items():
        if isinstance(data, dict):
            normalised[str(test_name)] = data
        else:
            normalised[str(test_name)] = {
                "value": data,
                "unit": "",
                "status": "extracted",
                "normal_range": {},
            }
    return normalised


def _lab_html(lab_result: Optional[Dict[str, Any]]) -> str:
    if not lab_result:
        return "<p>No lab analysis was performed.</p>"

    status = lab_result.get("status", "not_available")
    lab_data = _normalise_lab_data(lab_result)
    lab_context = _short_text(lab_result.get("lab_context", ""), 1100)
    raw_text = str(lab_result.get("raw_text", "") or "").strip()

    status_part = f"<p><strong>Status:</strong> {_escape(status)}</p>"
    raw_part = ""
    if raw_text:
        raw_part = (
            "<details class=\"ocr-details\">"
            "<summary>Short OCR excerpt for verification</summary>"
            f"<pre>{_escape(_short_text(raw_text, 900))}</pre>"
            "</details>"
        )

    if not lab_data:
        return (
            status_part
            + f"<p><strong>Lab summary:</strong> {_escape(lab_context or 'No structured lab values are available.')}</p>"
            + "<p class=\"small\">Full OCR text is intentionally not shown in the main report to keep the report concise.</p>"
            + raw_part
        )

    rows = []
    abnormal_rows = []
    for test_name, data in lab_data.items():
        normal_range = data.get("normal_range", {}) if isinstance(data.get("normal_range", {}), dict) else {}
        status_value = str(data.get("status", "unknown"))
        status_lower = status_value.lower().strip()
        row_class = " class=\"abnormal-row\"" if status_lower in {"high", "low", "abnormal", "critical"} else ""
        row = f"""
        <tr{row_class}>
          <td>{_escape(test_name)}</td>
          <td>{_escape(data.get('value', ''))}</td>
          <td>{_escape(data.get('unit', ''))}</td>
          <td>{_escape(status_value)}</td>
          <td>{_escape(normal_range.get('low', ''))} - {_escape(normal_range.get('high', ''))}</td>
        </tr>
        """
        rows.append(row)
        if status_lower in {"high", "low", "abnormal", "critical"}:
            abnormal_rows.append(f"<li>{_escape(test_name)}: {_escape(data.get('value', ''))} {_escape(data.get('unit', ''))} ({_escape(status_value)})</li>")

    abnormal_html = "<p>No abnormal extracted lab values were flagged.</p>" if not abnormal_rows else "<ul>" + "".join(abnormal_rows) + "</ul>"

    return f"""
    {status_part}
    <p><strong>Lab summary:</strong> {_escape(lab_context)}</p>
    <p><strong>Important flagged values:</strong></p>
    {abnormal_html}
    <table>
      <thead><tr><th>Test</th><th>Value</th><th>Unit</th><th>Status</th><th>Reference Range</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
    <p class=\"small\">Full OCR text is intentionally not shown in the main report to keep the report concise.</p>
    {raw_part}
    """

def _integrated_interpretation(xray_result: Optional[Dict[str, Any]], lab_result: Optional[Dict[str, Any]]) -> str:
    report = (xray_result or {}).get("report", {}) or {}
    text = " ".join([
        _display(report.get("findings", "")),
        _display(report.get("impression", "")),
        _display(report.get("abnormalities", [])),
    ]).lower()
    lab_context = str((lab_result or {}).get("lab_context", ""))
    lab_blob = lab_context.lower()

    imaging_suggestive = any(term in text for term in ["opacity", "consolidation", "infiltrate", "pneumonia"])
    inflammatory_labs = any(term in lab_blob for term in ["wbc", "crp", "neutrophils", "esr", "inflammatory", "infectious"])

    if imaging_suggestive and inflammatory_labs:
        return (
            "The X-ray findings and extracted lab context may support an inflammatory or infectious chest process when correlated clinically. "
            "This may be compatible with pneumonia in the appropriate clinical setting, but it is not a final diagnosis."
        )
    if imaging_suggestive:
        return (
            "The X-ray report includes opacity, consolidation, infiltrate, or a related abnormality. "
            "These findings require clinical correlation and radiologist review."
        )
    if inflammatory_labs:
        return (
            "The extracted lab context includes inflammatory or infection-related information, but imaging correlation and clinical review are still required."
        )
    return "No integrated imaging-lab conclusion can be made from the available structured context."


def build_patient_report_html(
    patient_info: Dict[str, Any],
    xray_result: Optional[Dict[str, Any]],
    lab_result: Optional[Dict[str, Any]],
    warnings: List[str],
    source: str,
) -> str:
    report = (xray_result or {}).get("report", {}) or {}
    alerts = (xray_result or {}).get("alerts", []) or []
    image_data = _image_data_uri((xray_result or {}).get("image_path"))
    image_html = f'<img src="{image_data}" class="case-image" />' if image_data else "<p>X-ray image not available in report.</p>"

    patient_rows = "".join(
        f"<tr><th>{_escape(key)}</th><td>{_escape(value)}</td></tr>"
        for key, value in patient_info.items()
    )
    warning_html = "<p>No warnings.</p>" if not warnings else "<ul>" + "".join(f"<li>{_escape(_public_warning(w))}</li>" for w in warnings) + "</ul>"

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f"AI Doctor Helper - Medical Report for {_escape(patient_info.get('patient_name', 'Patient'))}"
    if patient_info.get("patient_id"):
        title += f" ({_escape(patient_info.get('patient_id'))})"

    explanation = report.get("patient_explanation") or report.get("impression") or "No explanation available."
    integrated = _integrated_interpretation(xray_result, lab_result)

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 35px; color: #222; line-height: 1.5; }}
h1 {{ color: #1f3a5f; border-bottom: 3px solid #1f3a5f; padding-bottom: 10px; }}
h2 {{ color: #1f3a5f; margin-top: 28px; border-bottom: 1px solid #ccc; padding-bottom: 6px; }}
h3 {{ color: #1f3a5f; margin-top: 18px; }}
.box {{ border: 1px solid #ccc; border-radius: 8px; padding: 14px; background: #fafafa; margin: 12px 0; }}
.warning-box {{ border: 1px solid #e0a800; border-radius: 8px; padding: 12px; background: #fff8e1; margin: 12px 0; }}
.case-image {{ max-width: 100%; max-height: 520px; border: 1px solid #ccc; border-radius: 8px; margin: 10px 0; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 14px; }}
th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; vertical-align: top; }}
th {{ background: #f0f3f7; }}
pre {{ white-space: pre-wrap; background: #f6f6f6; border: 1px solid #ddd; padding: 12px; border-radius: 8px; max-height: 220px; overflow: auto; }}
.abnormal-row td {{ background: #fff3f3; }}
.ocr-details {{ margin-top: 12px; border: 1px dashed #b8c2cc; border-radius: 8px; padding: 10px; background: #fbfdff; }}
.ocr-details summary {{ cursor: pointer; font-weight: bold; color: #1f3a5f; }}
.small {{ color: #666; font-size: 13px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="small">Generated at: {_escape(generated_at)} | Source: {_escape(source)}</p>
<div class="box"><strong>Disclaimer:</strong> {_escape(DISCLAIMER)}</div>

<h2>Patient Information</h2>
<table><tbody>{patient_rows}</tbody></table>

<h2>Warnings</h2>
<div class="warning-box">{warning_html}</div>

<h2>Chest X-ray Analysis</h2>
{image_html}
<div class="box">
<p><strong>Status:</strong> {_escape((xray_result or {}).get('status', 'not_available'))}</p>
<p><strong>Image quality:</strong> {_escape(_display(report.get('image_quality', '')))}</p>
<p><strong>Estimated severity:</strong> {_escape(_display(report.get('severity', '')))}</p>
<p><strong>Findings:</strong> {_escape(_display(report.get('findings', '')))}</p>
<p><strong>Impression:</strong> {_escape(_display(report.get('impression', '')))}</p>
<p><strong>Detected findings:</strong></p>
<ul>{_list_html(report.get('abnormalities', []))}</ul>
<p><strong>Alerts:</strong></p>
<ul>{_alerts_html(alerts)}</ul>
<p><strong>Recommendations:</strong></p>
<ul>{_list_html(report.get('recommendations', []))}</ul>
</div>

<h2>Lab Report OCR and Context</h2>
{_lab_html(lab_result)}

<h2>Integrated Interpretation</h2>
<div class="box">{_escape(integrated)}</div>

<h2>Medical Explanation</h2>
<pre>{_escape(explanation)}</pre>

<div class="box"><strong>Final disclaimer:</strong> {_escape(DISCLAIMER)}</div>
</body>
</html>
"""


def default_report_filename(patient_info: Dict[str, Any]) -> str:
    name = str(patient_info.get("patient_name") or "patient").strip().lower().replace(" ", "_")
    patient_id = str(patient_info.get("patient_id") or "").strip().lower().replace("-", "_")
    safe_name = "".join(c if c.isalnum() or c == "_" else "_" for c in name).strip("_") or "patient"
    safe_id = "".join(c if c.isalnum() or c == "_" else "_" for c in patient_id).strip("_")
    if safe_id:
        return f"{safe_name}_{safe_id}_medical_report.html"
    return f"{safe_name}_medical_report.html"
