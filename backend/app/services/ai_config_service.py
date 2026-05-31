from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import app.core.config as config


RUNTIME_CONFIG_PATH = Path(
    os.getenv("AI_RUNTIME_CONFIG_PATH", str(config.CACHE_DIR / "ai_runtime_config.json"))
)


def _now_utc_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _normalize_url(url: str) -> str:
    cleaned = str(url or "").strip().rstrip("/")
    if not cleaned:
        raise ValueError("AI service URL is empty.")
    if not (cleaned.startswith("http://") or cleaned.startswith("https://")):
        raise ValueError("AI service URL must start with http:// or https://")
    return cleaned


def _read_runtime_config() -> Dict[str, Any]:
    if not RUNTIME_CONFIG_PATH.exists():
        return {}
    try:
        data = json.loads(RUNTIME_CONFIG_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _write_runtime_config(data: Dict[str, Any]) -> None:
    RUNTIME_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    RUNTIME_CONFIG_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def get_dynamic_ai_service_url() -> str:
    data = _read_runtime_config()
    return str(data.get("ai_service_url") or "").strip().rstrip("/")


def get_effective_ai_service_url() -> str:
    dynamic_url = get_dynamic_ai_service_url()
    if dynamic_url:
        return dynamic_url
    return str(getattr(config, "AI_SERVICE_URL", "") or os.getenv("AI_SERVICE_URL", "")).strip().rstrip("/")


def set_dynamic_ai_service_url(url: str, source: str = "manual_or_kaggle") -> Dict[str, Any]:
    cleaned = _normalize_url(url)
    data = _read_runtime_config()
    data.update(
        {
            "ai_service_url": cleaned,
            "source": source,
            "updated_at_utc": _now_utc_iso(),
        }
    )
    _write_runtime_config(data)
    return data


def clear_dynamic_ai_service_url() -> Dict[str, Any]:
    data = _read_runtime_config()
    previous = data.get("ai_service_url")
    data.pop("ai_service_url", None)
    data.update({"cleared_at_utc": _now_utc_iso(), "previous_ai_service_url": previous})
    _write_runtime_config(data)
    return data


def get_runtime_ai_config() -> Dict[str, Any]:
    data = _read_runtime_config()
    dynamic_url = str(data.get("ai_service_url") or "").strip().rstrip("/")
    env_url = str(getattr(config, "AI_SERVICE_URL", "") or os.getenv("AI_SERVICE_URL", "")).strip().rstrip("/")
    effective_url = dynamic_url or env_url

    return {
        "configured": bool(effective_url),
        "effective_ai_service_url": effective_url,
        "dynamic_ai_service_url": dynamic_url,
        "env_ai_service_url": env_url,
        "source": "dynamic" if dynamic_url else ("environment" if env_url else "not_configured"),
        "runtime_config_path": str(RUNTIME_CONFIG_PATH),
        "runtime_config": data,
        "defaults": {
            "AI_CHAT_MODE": os.getenv("AI_CHAT_MODE", "auto"),
            "AI_REQUEST_TIMEOUT_SECONDS": os.getenv("AI_REQUEST_TIMEOUT_SECONDS", "900"),
            "AI_CHAT_TIMEOUT_SECONDS": os.getenv("AI_CHAT_TIMEOUT_SECONDS", "30"),
            "AI_CHAT_RETRIES": os.getenv("AI_CHAT_RETRIES", "2"),
            "AI_XRAY_RESULT_POLLS": os.getenv("AI_XRAY_RESULT_POLLS", "8"),
            "AI_XRAY_RESULT_POLL_SECONDS": os.getenv("AI_XRAY_RESULT_POLL_SECONDS", "4"),
            "AI_LAB_OCR_RETRIES": os.getenv("AI_LAB_OCR_RETRIES", "3"),
            "AI_LAB_RESULT_POLLS": os.getenv("AI_LAB_RESULT_POLLS", "6"),
            "AI_LAB_RESULT_POLL_SECONDS": os.getenv("AI_LAB_RESULT_POLL_SECONDS", "5"),
            "AI_LAB_UPLOAD_MAX_SIDE": os.getenv("AI_LAB_UPLOAD_MAX_SIDE", "1800"),
            "AI_LAB_UPLOAD_JPEG_QUALITY": os.getenv("AI_LAB_UPLOAD_JPEG_QUALITY", "88"),
            "AI_WARMUP_TIMEOUT_SECONDS": os.getenv("AI_WARMUP_TIMEOUT_SECONDS", "900"),
        },
    }
