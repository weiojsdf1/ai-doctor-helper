from __future__ import annotations

from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

from app.services.ai_config_service import (
    clear_dynamic_ai_service_url,
    get_runtime_ai_config,
    set_dynamic_ai_service_url,
)

router = APIRouter(prefix="/ai/config", tags=["ai-config"])


class AIServiceURLIn(BaseModel):
    url: str = Field(..., description="Public Cloudflare/AI service URL, for example https://xxxxx.trycloudflare.com")
    source: str = Field(default="kaggle_cloudflare", description="Optional source label")


@router.get("/url")
def get_ai_service_url_config():
    """Return the currently effective AI service URL used by the backend."""
    return get_runtime_ai_config()


@router.post("/url")
def update_ai_service_url_config(payload: AIServiceURLIn):
    """Update the AI service URL dynamically without restarting the backend."""
    try:
        saved = set_dynamic_ai_service_url(payload.url, source=payload.source)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "status": "ok",
        "message": "AI service URL updated successfully.",
        "saved": saved,
        "config": get_runtime_ai_config(),
    }


@router.delete("/url")
def delete_ai_service_url_config():
    """Clear the dynamic AI service URL and fall back to environment settings if present."""
    cleared = clear_dynamic_ai_service_url()
    return {
        "status": "ok",
        "message": "Dynamic AI service URL cleared.",
        "cleared": cleared,
        "config": get_runtime_ai_config(),
    }
