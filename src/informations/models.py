from sqlalchemy import Table, Column, Integer, String, MetaData

from database import Base

metadata = MetaData()

information = Table(
    "information",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("paragraph", String),
    Column("title", String),
    Column("money", Integer),

)


class Information(Base):
    __tablename__ = "information"

    id = Column(Integer, primary_key=True)
    paragraph = Column(String)
    title = Column(String)
    money = Column(Integer)
