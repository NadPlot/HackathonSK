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


@app.get("/")
async def root():
    return {"message": "REST API FSTR"}


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

    new_add = Added(date_added=date_added, raw_data=raw, images=dict(raw_data.images), status='new')
    #db.add(images, new_add)
    db.add(new_add)
    db.commit()
    return new_add


# MVP2: получить одну запись (перевал) по её id.
@app.get("/submitData/{id}/", response_model=schemas.Added)
def read_added_id(id: int, db: Session = Depends(get_db)):
    added = crud.get_added_id(db, id=id)
    return added


# MVP2: получить статус модерации отправленных данных
@app.get("/submitData/{id}/status", response_model=schemas.Added, response_model_exclude={"date_added", "raw_data", "images"})
def read_added_id(id: int, db: Session = Depends(get_db)):
    return crud.get_added_id(db, id=id)