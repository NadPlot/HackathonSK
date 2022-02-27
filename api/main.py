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

new = {
    "id": "12865",
   "beautyTitle": "пер. ",
    "title": "New",
    "other_titles": "Триев",
    "connect": "",

    "add_time": "2021-09-25 13:18:13",

    "user": {
        "id": "vpupkin",
        "email": "user@email.tld",
        "phone": "79031234567",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович"
        },

   "coords":{
       "latitude": "35.3842",
       "longitude": "17.1525",
       "height": "1200"},

  "type": "pass",

  "level":{
      "winter": "1b",
      "summer": "",
      "autumn": "1А",
      "spring": ""},

   "images": [
       {'url':"http://...", 'title':"Подъём. Фото №1"},
       {'url':"http://...", 'title':"Подъём. Фото №2"},
       {'url':"http://...", 'title':"Седловина"},
       {'url':"http://...", 'title':"Спуск. Фото №99"},
       {'url':"http://...", 'title':"Спуск. Фото №99"}]
}


# MVP1: отправить информацию об объекте на сервер
@app.post("/submitData/", response_model=schemas.AddedCreate)
def add_to_added(raw_data: schemas.AddedRaw, db: Session = Depends(get_db)):
    date_added = raw_data.add_time
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

    images = schemas.Images(
        sedlo=raw_data.images[0],
        Nord=raw_data.images[1],
        West=raw_data.images[2],
        South=raw_data.images[3],
        East=raw_data.images[4]
    )
    new_add = schemas.AddedBase(date_added=date_added, raw_data=raw, images=images, status='new')
    return new_add


# MVP2: получить одну запись (перевал) по её id.
@app.get("/submitData/{id}/", response_model=schemas.AddedIDOut)
def read_added_id(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_id(db, id=id)
    return added



@app.get("/areas/{id}", response_model=schemas.Areas)
def read_areas(id: int, db: Session = Depends(get_db)):
    areas = crud.get_areas(db, id=id)
    return areas