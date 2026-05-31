from __future__ import annotations

from fastapi import APIRouter

from app.services.ai_client import ai_client

router = APIRouter(prefix="/ai", tags=["ai-service"])


@router.get("/health")
def ai_service_health():
    """Check whether the configured remote AI service is reachable."""
    return ai_client.check_remote_service()


@router.post("/warmup")
def ai_service_warmup():
    """Warm up the remote model before a live demo or analysis session."""
    return ai_client.warmup_remote_service()
