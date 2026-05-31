from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    answer: str
    note: str
    source: Optional[str] = None


class ChatMessageRead(BaseModel):
    id: int
    patient_db_id: int
    role: str
    content: str
    created_at: datetime

    model_config = {"from_attributes": True}
