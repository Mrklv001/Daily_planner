from sqlalchemy.orm import Session
from app import models, schemas


def get_entry(db: Session, entry_id: int):
    return db.query(models.DiaryEntry).filter(models.DiaryEntry.id == entry_id).first()


def get_entries(db: Session):
    return db.query(models.DiaryEntry).all()


def create_entry(db: Session, entry: schemas.EntryCreate):
    db_entry = models.DiaryEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def update_entry(db: Session, entry_id: int, entry_data: schemas.EntryUpdate):
    db_entry = get_entry(db, entry_id)
    if db_entry:
        db_entry.title = entry_data.title
        db_entry.content = entry_data.content
        db_entry.is_done = entry_data.is_done
        db.commit()
        db.refresh(db_entry)
    return db_entry


def delete_entry(db: Session, entry_id: int):
    db_entry = get_entry(db, entry_id)
    if db_entry:
        db.delete(db_entry)
        db.commit()
    return db_entry
