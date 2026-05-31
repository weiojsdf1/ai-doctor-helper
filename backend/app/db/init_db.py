from app.db.base import Base
from app.db.session import engine

# Import models so SQLAlchemy registers them before creating tables.
from app.models.patient import Patient  # noqa: F401
from app.models.file_record import FileRecord  # noqa: F401
from app.models.report_record import ReportRecord  # noqa: F401
from app.models.chat_message import ChatMessage  # noqa: F401


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
