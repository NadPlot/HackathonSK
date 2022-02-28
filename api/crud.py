from sqlalchemy.orm import Session
from .database import Areas, Added


# MVP2: получить одну запись (перевал) по её id.
def get_added_id(db: Session, id: int):
    return db.query(Added).filter(Added.id == id).first()

#for testing
def get_areas(db: Session, id: int):
    return db.query(Areas).filter(Areas.id == id).first()
