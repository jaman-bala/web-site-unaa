from sqlalchemy import Column, Integer, String, Text, DateTime, func, TIMESTAMP, MetaData, Table
from database import Base

metadata = MetaData()

news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", Text),
    Column("img", String, nullable=True),
    Column("publication_date", TIMESTAMP),
)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    img = Column(String, nullable=True)
    publication_date = Column(DateTime(timezone=True), server_default=func.now())

    def __str__(self):
        return f"Название {self.title}"
