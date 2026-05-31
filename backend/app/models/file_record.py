from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class FileRecord(Base):
    __tablename__ = "file_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    patient_db_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), index=True)
    file_type: Mapped[str] = mapped_column(String(30), index=True)  # xray, lab, other
    original_filename: Mapped[str] = mapped_column(String(255))
    stored_filename: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(String(500))
    content_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient", back_populates="files")
