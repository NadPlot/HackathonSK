import datetime
from typing import Optional
from pydantic import BaseModel


# таблица pereval_images
class ImagesBase(BaseModel):
    date_added: datetime.datetime
    img: Optional[str] = None


class ImageCreate(ImagesBase):
    pass


class Images(ImagesBase):
    id: int

    class Config:
        orm_mode = True


# для поля raw_data (табл pereval_added):
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
    sedlo: Optional[list] = None
    Nord: Optional[list] = None
    West: Optional[list] = None
    South: Optional[list]= None
    East: Optional[list] = None


# столбец raw_data (pereval_added)
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


# поля, отправленные в теле запроса (JSON)
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
    images: Optional[list[dict]] = None


# MVP1: отправить информацию об объекте на сервер
class AddedBase(BaseModel):
    date_added: datetime.datetime
    raw_data: RawData
    images: Images
    status: Optional[str] = None


class AddedCreate(AddedBase):
    id: int


class Added(AddedBase):
    pass

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


# таблица pereval_areas
class AreasBase(BaseModel):
    title: Optional[str] = None
    id_parent: Optional[int] = None


class Areas(AreasBase):
    id: int

    class Config:
        orm_mode = True