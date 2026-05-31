from datetime import datetime
from pydantic import BaseModel


class ReportRecordRead(BaseModel):
    id: int
    patient_db_id: int
    report_type: str
    filename: str
    file_path: str
    created_at: datetime

    model_config = {"from_attributes": True}
