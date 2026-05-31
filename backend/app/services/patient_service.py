from datetime import datetime
from pathlib import Path
import json
import re

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.config import PATIENTS_STORAGE_DIR
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u0600-\u06FF]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_") or "patient"


def get_current_month_folder() -> str:
    return datetime.utcnow().strftime("%Y-%m")


def generate_patient_id(db: Session, month_folder: str | None = None) -> str:
    month_folder = month_folder or get_current_month_folder()
    compact_month = month_folder.replace("-", "")

    count = (
        db.query(func.count(Patient.id))
        .filter(Patient.monthly_folder == month_folder)
        .scalar()
    ) or 0

    return f"PT-{compact_month}-{count + 1:03d}"


def create_patient_folders(patient_name: str, patient_id: str, month_folder: str) -> Path:
    safe_name = _slugify(patient_name)
    safe_id = _slugify(patient_id)

    patient_folder = PATIENTS_STORAGE_DIR / month_folder / f"{safe_name}_{safe_id}"

    (patient_folder / "xrays").mkdir(parents=True, exist_ok=True)
    (patient_folder / "labs").mkdir(parents=True, exist_ok=True)
    (patient_folder / "reports").mkdir(parents=True, exist_ok=True)
    (patient_folder / "outputs").mkdir(parents=True, exist_ok=True)
    (patient_folder / "chat").mkdir(parents=True, exist_ok=True)

    return patient_folder


def write_patient_info_files(patient: Patient) -> None:
    folder = Path(patient.patient_folder)
    folder.mkdir(parents=True, exist_ok=True)

    data = {
        "patient_id": patient.patient_id,
        "patient_name": patient.patient_name,
        "age": patient.age,
        "sex": patient.sex,
        "phone": patient.phone,
        "symptoms_or_notes": patient.symptoms_or_notes,
        "monthly_folder": patient.monthly_folder,
        "created_at": patient.created_at.isoformat() if patient.created_at else None,
        "updated_at": patient.updated_at.isoformat() if patient.updated_at else None,
    }

    with open(folder / "patient_info.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    lines = [
        f"Patient ID: {patient.patient_id}",
        f"Patient Name: {patient.patient_name}",
        f"Age: {patient.age if patient.age is not None else ''}",
        f"Sex: {patient.sex or ''}",
        f"Phone: {patient.phone or ''}",
        f"Symptoms / Notes: {patient.symptoms_or_notes or ''}",
        f"Created At: {data['created_at'] or ''}",
        f"Updated At: {data['updated_at'] or ''}",
    ]

    with open(folder / "patient_info.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def create_patient(db: Session, patient_in: PatientCreate) -> Patient:
    month_folder = get_current_month_folder()
    patient_id = generate_patient_id(db, month_folder)
    patient_folder = create_patient_folders(patient_in.patient_name, patient_id, month_folder)

    patient = Patient(
        patient_id=patient_id,
        patient_name=patient_in.patient_name,
        age=patient_in.age,
        sex=patient_in.sex,
        phone=patient_in.phone,
        symptoms_or_notes=patient_in.symptoms_or_notes,
        monthly_folder=month_folder,
        patient_folder=str(patient_folder),
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)
    write_patient_info_files(patient)
    return patient


def get_patient_by_patient_id(db: Session, patient_id: str) -> Patient | None:
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()


def update_patient(db: Session, patient: Patient, patient_in: PatientUpdate) -> Patient:
    update_data = patient_in.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(patient, key, value)

    db.add(patient)
    db.commit()
    db.refresh(patient)
    write_patient_info_files(patient)
    return patient
