from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False, default="pending")
    priority = Column(Integer, nullable=False, default=3)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
