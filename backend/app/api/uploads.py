from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.file_record import FileRecord
from app.schemas.file_record import FileRecordRead
from app.services.file_service import save_patient_file
from app.services.patient_service import get_patient_by_patient_id

router = APIRouter(prefix="/patients/{patient_id}/files", tags=["uploads"])


@router.post("/xray", response_model=FileRecordRead, status_code=status.HTTP_201_CREATED)
def upload_single_xray_file(
    patient_id: str,
    file: Annotated[UploadFile, File(description="Select one Chest X-ray image file")],
    db: Session = Depends(get_db),
):
    """
    Upload one Chest X-ray image for a patient.

    Use this endpoint first when testing in Swagger because it always shows
    a normal file picker button.
    """
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return save_patient_file(db, patient, file, "xray")


@router.post("/lab", response_model=FileRecordRead, status_code=status.HTTP_201_CREATED)
def upload_single_lab_file(
    patient_id: str,
    file: Annotated[UploadFile, File(description="Select one lab report image file")],
    db: Session = Depends(get_db),
):
    """
    Upload one lab report image for a patient.

    Use this endpoint first when testing in Swagger because it always shows
    a normal file picker button.
    """
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return save_patient_file(db, patient, file, "lab")


@router.post("/xrays", response_model=list[FileRecordRead], status_code=status.HTTP_201_CREATED)
def upload_multiple_xray_files(
    patient_id: str,
    files: Annotated[list[UploadFile], File(description="Select one or more Chest X-ray image files")],
    db: Session = Depends(get_db),
):
    """
    Upload multiple Chest X-ray images for a patient.
    """
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return [save_patient_file(db, patient, file, "xray") for file in files]


@router.post("/labs", response_model=list[FileRecordRead], status_code=status.HTTP_201_CREATED)
def upload_multiple_lab_files(
    patient_id: str,
    files: Annotated[list[UploadFile], File(description="Select one or more lab report image files")],
    db: Session = Depends(get_db),
):
    """
    Upload multiple lab report images for a patient.
    """
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return [save_patient_file(db, patient, file, "lab") for file in files]


@router.get("", response_model=list[FileRecordRead])
def list_patient_files(patient_id: str, db: Session = Depends(get_db)):
    """
    List all uploaded files for one patient.
    """
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")

    return (
        db.query(FileRecord)
        .filter(FileRecord.patient_db_id == patient.id)
        .order_by(FileRecord.uploaded_at.desc())
        .all()
    )
