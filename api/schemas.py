from typing import Optional
from pydantic import BaseModel


class AreasBase(BaseModel):
    title: Optional[str] = None
    id_parent: Optional[int] = None


class AreasCreate(AreasBase):
    pass


class Areas(AreasBase):
    id: int

    class Config:
        orm_mode = True