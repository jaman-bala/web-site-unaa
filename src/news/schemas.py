from pydantic import BaseModel
from datetime import datetime


class NewsBase(BaseModel):
    title: str
    description: str
    img: str


class NewsCreate(BaseModel):
    title: str
    description: str
    img: str
    publication_date: datetime


class News(NewsBase):
    id: int

    class Config:
        orm_mode = True

