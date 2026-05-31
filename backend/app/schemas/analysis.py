from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    status: str
    message: str
    patient_id: str
    available_xray_files: int
    available_lab_files: int
    warnings: list[str] = []
    source: Optional[str] = None
    cache_key: Optional[str] = None
    report_id: Optional[int] = None
    report_filename: Optional[str] = None
    report_download_url: Optional[str] = None
