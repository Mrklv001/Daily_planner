from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, func
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)

    priority = Column(Integer, default=3)
    tags = Column(ARRAY(String), default=[])
    due_date = Column(Date, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
