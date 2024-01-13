from pydantic import BaseModel


class InformationCreate(BaseModel):
    paragraph: str
    title: str
    money: int


class InformationOUT(InformationCreate):
    id: int