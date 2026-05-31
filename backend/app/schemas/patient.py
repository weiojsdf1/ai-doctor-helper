from datetime import datetime
from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    patient_name: str = Field(..., min_length=1, max_length=150)
    age: int | None = Field(default=None, ge=0, le=130)
    sex: str | None = Field(default=None, max_length=30)
    phone: str | None = Field(default=None, max_length=50)
    symptoms_or_notes: str | None = None


class PatientUpdate(BaseModel):
    patient_name: str | None = Field(default=None, min_length=1, max_length=150)
    age: int | None = Field(default=None, ge=0, le=130)
    sex: str | None = Field(default=None, max_length=30)
    phone: str | None = Field(default=None, max_length=50)
    symptoms_or_notes: str | None = None


class PatientRead(BaseModel):
    id: int
    patient_id: str
    patient_name: str
    age: int | None
    sex: str | None
    phone: str | None
    symptoms_or_notes: str | None
    monthly_folder: str
    patient_folder: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
