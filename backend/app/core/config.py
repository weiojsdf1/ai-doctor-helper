from pathlib import Path
import os

# Demo-safe defaults.
# These make the backend work without manually typing many `set ...` commands.
os.environ.setdefault("AI_CHAT_MODE", "auto")
os.environ.setdefault("AI_REQUEST_TIMEOUT_SECONDS", "900")
os.environ.setdefault("AI_CHAT_TIMEOUT_SECONDS", "30")
os.environ.setdefault("AI_CHAT_RETRIES", "2")
os.environ.setdefault("AI_XRAY_RESULT_POLLS", "8")
os.environ.setdefault("AI_XRAY_RESULT_POLL_SECONDS", "4")
os.environ.setdefault("AI_LAB_OCR_RETRIES", "3")
os.environ.setdefault("AI_LAB_RESULT_POLLS", "6")
os.environ.setdefault("AI_LAB_RESULT_POLL_SECONDS", "5")
os.environ.setdefault("AI_LAB_UPLOAD_MAX_SIDE", "1800")
os.environ.setdefault("AI_LAB_UPLOAD_JPEG_QUALITY", "88")
os.environ.setdefault("AI_WARMUP_TIMEOUT_SECONDS", "900")


BASE_DIR = Path(__file__).resolve().parents[2]
PROJECT_ROOT = BASE_DIR.parent

APP_NAME = "AI Doctor Helper Backend"
APP_VERSION = "1.3.0"

DATABASE_URL = f"sqlite:///{PROJECT_ROOT / 'app.db'}"

STORAGE_DIR = PROJECT_ROOT / "storage"
PATIENTS_STORAGE_DIR = STORAGE_DIR / "patients"
REPORTS_STORAGE_DIR = STORAGE_DIR / "reports"
CACHE_DIR = PROJECT_ROOT / "cache"
ANALYSIS_CACHE_DIR = CACHE_DIR / "analysis"

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "").rstrip("/")
AI_REQUEST_TIMEOUT_SECONDS = int(os.getenv("AI_REQUEST_TIMEOUT_SECONDS", "900"))
AI_CHAT_MODE = os.getenv("AI_CHAT_MODE", "auto").lower().strip()  # auto | remote | local

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
SUPPORTED_REPORT_EXTENSIONS = {".html", ".pdf", ".txt", ".json"}

DISCLAIMER = (
    "This system is for educational and research purposes only. "
    "It does not provide a final medical diagnosis. "
    "Final interpretation must be performed by a qualified physician or radiologist."
)
