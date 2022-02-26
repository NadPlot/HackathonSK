from sqlalchemy.orm import Session
from .database import Areas


def get_areas(db: Session, id: int):
    return db.query(Areas).filter(Areas.id == id).first()