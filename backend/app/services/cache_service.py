from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any, Dict, Optional

from app.core.config import ANALYSIS_CACHE_DIR


def file_sha256(path: str | Path) -> str:
    file_path = Path(path)
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_case_hash(xray_path: Optional[str], lab_path: Optional[str]) -> str:
    parts = []
    if xray_path:
        parts.append(file_sha256(xray_path))
    else:
        parts.append("no_xray")
    if lab_path:
        parts.append(file_sha256(lab_path))
    else:
        parts.append("no_lab")
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()


def cache_dir_for_key(cache_key: str) -> Path:
    return ANALYSIS_CACHE_DIR / cache_key


def load_cache(cache_key: str) -> Optional[Dict[str, Any]]:
    folder = cache_dir_for_key(cache_key)
    manifest = folder / "manifest.json"
    if not manifest.exists():
        return None
    try:
        return json.loads(manifest.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_cache(cache_key: str, data: Dict[str, Any], files_to_copy: Optional[Dict[str, str]] = None) -> None:
    folder = cache_dir_for_key(cache_key)
    folder.mkdir(parents=True, exist_ok=True)
    manifest_data = dict(data)
    copied = {}
    for name, path in (files_to_copy or {}).items():
        source = Path(path)
        if source.exists() and source.is_file():
            dest = folder / source.name
            shutil.copy2(source, dest)
            copied[name] = str(dest)
    manifest_data["cached_files"] = copied
    (folder / "manifest.json").write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")
