import json

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


# MVP1: отправить информацию об объекте на сервер
@app.post("/submitData/", response_model=schemas.AddedCreate)
def add_to_added(raw_data: schemas.RawData, db: Session = Depends(get_db)):
    pass
    #return id


# MVP2: получить одну запись (перевал) по её id.
@app.get("/submitData/{id}/", response_model=schemas.AddedIDOut)
def read_added_id(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_id(db, id=id)
    return added\



@app.get("/areas/{id}", response_model=schemas.Areas)
def read_areas(id: int, db: Session = Depends(get_db)):
    areas = crud.get_areas(db, id=id)
    return areas