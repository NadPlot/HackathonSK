import datetime
from typing import Optional
from pydantic import BaseModel


# pereval_areas
class AreasBase(BaseModel):
    title: Optional[str] = None
    id_parent: Optional[int] = None


class AreasCreate(AreasBase):
    pass


class Areas(AreasBase):
    id: int

    class Config:
        orm_mode = True

# таблица pereval_images
class ImagesBase(BaseModel):
    id: int
    date_added: datetime.date
    img: bytes


# классы для табл pereval_added:
class User(BaseModel):
    id: str
    email: str
    phone: int
    fam: str
    name: str
    otc: str


class Coords(BaseModel):
    latitude: str
    longitude: str
    height: str


class Level(BaseModel):
    winter: Optional[str] = None
    summer: Optional[str] = None
    autumn: Optional[str] = None
    spring: Optional[str] = None


class Images(BaseModel):
    sedlo: Optional[dict] = None
    Nord: Optional[dict] = None
    West: Optional[dict] = None
    South: Optional[dict]= None
    East: Optional[dict] = None


class RawData(BaseModel):
    pereval_id: int
    beautyTitle: str
    title: str
    other_titles: Optional[str] = None
    connect: Optional[str] = None
    user: User
    coords: Coords
    type: Optional[str] = 'pass'
    level: Level


class AddedBase(BaseModel):
    date_added: datetime.date
    raw_data: RawData
    images: Images
    status: Optional[str] = None


# поля, отправленные в тело запроса (JSON)
class AddedRaw(BaseModel):
    id: int
    beautyTitle: str
    title: str
    other_titles: Optional[str] = None
    connect: Optional[str]
    add_time: str
    user: User
    coords: Coords
    type: Optional[str] = 'pass'
    level: Level
    images: Images


# MVP1: отправить информацию об объекте на сервер
class AddedCreate(AddedBase):
    id: int

    class Config:
        orm_mode = True


class AddedRawDataOut(BaseModel):
    raw_data: RawData

    class Config:
        orm_mode = True


# MVP2: получить одну запись (перевал) по её id.
class AddedIDOut(AddedBase):
    id: int

    class Config:
        orm_mode = True