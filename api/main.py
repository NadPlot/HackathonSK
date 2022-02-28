import json

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas

from .database import SessionLocal, engine, Added, Images

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# MVP1: отправить информацию об объекте на сервер
@app.post("/submitData/", response_model=schemas.Added)
def add_to_added(raw_data: schemas.AddedRaw, db: Session = Depends(get_db)):
    date_added = raw_data.add_time  # get str - need datetime!!!
    pereval_id = raw_data.id
    raw = schemas.RawData(
        pereval_id=pereval_id,
        beautyTitle=raw_data.beautyTitle,
        title=raw_data.title,
        other_titles=raw_data.other_titles,
        connect=raw_data.connect,
        user=raw_data.user,
        coords=raw_data.coords,
        type=raw_data.type,
        level=raw_data.level
    )

    # images = Images(
    #     date_added=date_added,
    #     img=raw_data.images
    # )

    new_add = Added(id=2, date_added=date_added, raw_data=raw, images=raw_data.images, status='new')
    #db.add(images, new_add)
    db.commit()
    return new_add


# MVP2: получить одну запись (перевал) по её id.
@app.get("/submitData/{id}/", response_model=schemas.AddedIDOut)
async def read_added_id(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_id(db, id=id)
    return added



@app.get("/areas/{id}", response_model=schemas.Areas)
def read_areas(id: int, db: Session = Depends(get_db)):
    areas = crud.get_areas(db, id=id)
    return areas