from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientRead, PatientUpdate
from app.services.patient_service import create_patient, get_patient_by_patient_id, update_patient

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def create_new_patient(patient_in: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient_in)


@router.get("", response_model=list[PatientRead])
def list_patients(db: Session = Depends(get_db)):
    return db.query(Patient).order_by(Patient.created_at.desc()).all()


@router.get("/{patient_id}", response_model=PatientRead)
def get_patient(patient_id: str, db: Session = Depends(get_db)):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")
    return patient


@router.put("/{patient_id}", response_model=PatientRead)
def edit_patient(patient_id: str, patient_in: PatientUpdate, db: Session = Depends(get_db)):
    patient = get_patient_by_patient_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found.")
    return update_patient(db, patient, patient_in)
