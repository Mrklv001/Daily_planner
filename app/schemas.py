from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date


class EntryBase(BaseModel):
    title: str
    content: str
    priority: int = Field(default=3, ge=1, le=5)
    tags: List[str] = []
    due_date: Optional[date] = None


class EntryCreate(EntryBase):
    pass


class EntryUpdate(EntryBase):
    is_done: bool


class Entry(EntryBase):
    id: int
    is_done: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
