from datetime import datetime
from pydantic import BaseModel


class FileRecordRead(BaseModel):
    id: int
    patient_db_id: int
    file_type: str
    original_filename: str
    stored_filename: str
    file_path: str
    content_type: str | None
    uploaded_at: datetime

    model_config = {"from_attributes": True}
