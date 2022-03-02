from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine, Added, Images
from fastapi import FastAPI


description = """
для мобильного приложения ФСТР. 🚀

## Отправка информации на сервер о перевале

"""


app = FastAPI(
    title="REST API FSTR",
    description=description,

)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# for testing
a = {
  "id": 12865,
  "beautyTitle": "пер.",
  "title": "Новый",
  "other_titles": "перевал",
  "connect": "",
  "add_time": "2021-09-25 13:18:13",
  "user": {
    "id": "vpupkin",
    "email": "user@email.tld",
    "phone": 79031234567,
    "fam": "Пупкин",
    "name": "Василий",
    "otc": "Иванович"
  },
  "coords": {
    "latitude": "12.5565",
    "longitude": "7.5546",
    "height": "1205"
  },
  "type": "pass",
  "level": {
    "winter": "1А",
    "summer": "",
    "autumn": "2А",
    "spring": ""
  },
  "images": [
      {"url":"http://...", "title":"Подъём. Фото №1"},
      {"url":"http://...", "title":"Подъём. Фото №2"},
      {"url":"http://...", "title":"Седловина"},
      {"url":"http://...", "title":"Спуск. Фото №99"},
      {"url":"http://...", "title":"Спуск. Фото №99"}
  ]
}


# MVP1: отправить информацию об объекте на сервер
@app.post("/submitData/", response_model=schemas.Added)
def add_to_added(raw_data: schemas.AddedRaw, db: Session = Depends(get_db)):
    date_added = raw_data.add_time
    pereval_id = raw_data.id
    user = dict(raw_data.user)
    raw = dict(schemas.RawData(
        pereval_id=pereval_id,
        beautyTitle=raw_data.beautyTitle,
        title=raw_data.title,
        other_titles=raw_data.other_titles,
        connect=raw_data.connect,
        user=user,
        coords=raw_data.coords,
        type=raw_data.type,
        level=raw_data.level
    ))

    # images = Images(
    #     date_added=date_added,
    #     img=raw_data.images
    # )

    new_add = Added(date_added=date_added, raw_data=raw, images=raw_data.images, status='new')
    #db.add(images, new_add)
    db.add(new_add)
    db.commit()
    return new_add


# MVP2: получить одну запись (перевал) по её id.
@app.get("/submitData/{id}/", response_model=schemas.AddedIDOut)
async def read_added_id(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_id(db, id=id)
    return added