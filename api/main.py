from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas

from .database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/areas/{id}", response_model=schemas.Areas)
def read_areas(id: int, db: Session = Depends(get_db)):
    areas = crud.get_areas(db, id=id)
    return areas


@app.get("/status/{id}", response_model=schemas.AddedStatusOut)
def read_added_status(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_status(db, id=id)
    return added