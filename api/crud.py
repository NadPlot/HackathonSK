from sqlalchemy.orm import Session
from .database import Areas, Added


def get_areas(db: Session, id: int):
    return db.query(Areas).filter(Areas.id == id).first()


def get_added(db: Session, id: int):
    return db.query(Added).filter(Added.id == id)

def get_added_status(db: Session, id: int):
    return db.query(Added).filter(Added.id == id).first()