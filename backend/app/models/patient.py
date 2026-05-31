from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    patient_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    patient_name: Mapped[str] = mapped_column(String(150), index=True)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sex: Mapped[str | None] = mapped_column(String(30), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    symptoms_or_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    monthly_folder: Mapped[str] = mapped_column(String(20), index=True)
    patient_folder: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    files = relationship("FileRecord", back_populates="patient", cascade="all, delete-orphan")
    reports = relationship("ReportRecord", back_populates="patient", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="patient", cascade="all, delete-orphan")
