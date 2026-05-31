from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ai_config, ai_status, analysis, chat, patients, reports, uploads
from app.core.config import APP_NAME, APP_VERSION, DISCLAIMER, STORAGE_DIR
from app.db.init_db import init_db

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Backend API for AI Doctor Helper patient management and future AI integration.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    init_db()


@app.get("/")
def root():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
        "disclaimer": DISCLAIMER,
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(ai_config.router, prefix="/api")
app.include_router(ai_status.router, prefix="/api")
app.include_router(patients.router, prefix="/api")
app.include_router(uploads.router, prefix="/api")
app.include_router(reports.router, prefix="/api")
app.include_router(analysis.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
