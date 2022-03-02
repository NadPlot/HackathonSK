from sqlalchemy.orm import Session
from .database import Added


# MVP2: получить одну запись (перевал) по её id.
def get_added_id(db: Session, id: int):
    return db.query(Added).filter(Added.id == id).first()


# MVP2: получить статус модерации отправленных данных
def get_added_status(db: Session, id: int):
    status = db.query(Added.status).filter(Added.id == id)

    return status