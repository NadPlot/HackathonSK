from sqlalchemy.orm import Session
from .database import Areas, Added, Images
from . import schemas


def add_raw_data(db: Session, raw_data: schemas.AddedRaw):
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

    images = Images(
        date_added=date_added
    )

    new_add = Added(date_added=date_added, raw_data=raw, status='new')
    db.add(images, new_add)
    db.commit()
    return images, new_add


# MVP2: получить одну запись (перевал) по её id.
def get_added_id(db: Session, id: int):
    return db.query(Added).filter(Added.id == id).first()

def get_areas(db: Session, id: int):
    return db.query(Areas).filter(Areas.id == id).first()
