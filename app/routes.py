from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/entries/", response_model=schemas.Entry)
def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db, entry)


@router.get("/entries/", response_model=list[schemas.Entry])
def read_entries(db: Session = Depends(get_db)):
    return crud.get_entries(db)


@router.get("/entries/{entry_id}", response_model=schemas.Entry)
def read_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = crud.get_entry(db, entry_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry


@router.put("/entries/{entry_id}", response_model=schemas.Entry)
def update_entry(entry_id: int, entry: schemas.EntryUpdate, db: Session = Depends(get_db)):
    db_entry = crud.update_entry(db, entry_id, entry)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry


@router.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = crud.delete_entry(db, entry_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"ok": True}
