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
    latitude: float
    longitude: float
    height: float


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


class AddedCreate(AddedBase):
    id: int


class AddedRawDataOut(BaseModel):
    raw_data: RawData

    class Config:
        orm_mode = True


class AddedIDOut(AddedBase):
    id: int

    class Config:
        orm_mode = True