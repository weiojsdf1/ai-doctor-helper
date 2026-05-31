from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.report_record import ReportRecord
from app.schemas.report import ReportRecordRead
from app.services.file_service import ensure_existing_file, save_patient_report
from app.services.patient_service import get_patient_by_patient_id

router = APIRouter(prefix="/patients/{patient_id}/reports", tags=["reports"])


@router.post("", response_model=ReportRecordRead, status_code=status.HTTP_201_CREATED)
def upload_report(
    patient_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return save_patient_report(db, patient, file)


@router.get("", response_model=list[ReportRecordRead])
def list_reports(patient_id: str, db: Session = Depends(get_db)):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return (
        db.query(ReportRecord)
        .filter(ReportRecord.patient_db_id == patient.id)
        .order_by(ReportRecord.created_at.desc())
        .all()
    )


@router.get("/{report_id}/download")
def download_report(patient_id: str, report_id: int, db: Session = Depends(get_db)):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    report = (
        db.query(ReportRecord)
        .filter(ReportRecord.id == report_id, ReportRecord.patient_db_id == patient.id)
        .first()
    )
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found.")

    file_path = ensure_existing_file(report.file_path)
    return FileResponse(path=file_path, filename=report.filename)
