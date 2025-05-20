from pydantic import BaseModel


class EntryBase(BaseModel):
    title: str
    content: str


class EntryCreate(EntryBase):
    pass


class EntryUpdate(EntryBase):
    is_done: bool


class Entry(EntryBase):
    id: int
    is_done: bool

    class Config:
        orm_mode = True
