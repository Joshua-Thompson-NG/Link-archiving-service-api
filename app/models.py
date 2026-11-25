from datetime import datetime, timezone

from pydantic import HttpUrl
from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Snapshot(Base):
    __tablename__ = "snapshots"

    id: Mapped[str] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda : datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False
    )