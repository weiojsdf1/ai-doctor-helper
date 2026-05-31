from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.analysis import AnalysisResponse
from app.services.ai_client import ai_client
from app.services.patient_service import get_patient_by_patient_id

router = APIRouter(prefix="/patients/{patient_id}/analysis", tags=["analysis"])


def _get_patient_or_404(patient_id: str, db: Session):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")
    return patient


def _to_response(result: dict) -> AnalysisResponse:
    return AnalysisResponse(
        status=result.get("status", "unknown"),
        message=result.get("message", ""),
        patient_id=result.get("patient_id", ""),
        available_xray_files=int(result.get("available_xray_files", 0)),
        available_lab_files=int(result.get("available_lab_files", 0)),
        warnings=result.get("warnings", []) or [],
        source=result.get("source"),
        cache_key=result.get("cache_key"),
        report_id=result.get("report_id"),
        report_filename=result.get("report_filename"),
        report_download_url=result.get("report_download_url"),
    )


@router.post("/xray", response_model=AnalysisResponse)
def analyze_patient_xray(patient_id: str, db: Session = Depends(get_db)):
    patient = _get_patient_or_404(patient_id, db)
    return _to_response(ai_client.analyze_xray_only(db, patient))


@router.post("/lab", response_model=AnalysisResponse)
def analyze_patient_lab_and_merge(patient_id: str, db: Session = Depends(get_db)):
    patient = _get_patient_or_404(patient_id, db)
    return _to_response(ai_client.analyze_lab_and_merge(db, patient))


@router.post("/start", response_model=AnalysisResponse)
def start_patient_analysis(patient_id: str, db: Session = Depends(get_db)):
    patient = _get_patient_or_404(patient_id, db)
    return _to_response(ai_client.analyze_patient(db, patient))
