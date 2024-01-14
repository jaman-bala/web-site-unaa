from sqlalchemy import Column, Integer, String, Text, DateTime, func, TIMESTAMP, MetaData, Table
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType, ImageType
from database import Base

metadata = MetaData()
storage_img = FileSystemStorage(path="./static/images")
storage_file = FileSystemStorage(path="./static/file")

news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", Text),
    Column("img", ImageType(storage=storage_img), nullable=True),
    Column("file", FileType(storage=storage_file), nullable=True),
    Column("publication_date", TIMESTAMP),
)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    img = Column(ImageType(storage=storage_img), nullable=True)
    file = Column(FileType(storage=storage_file), nullable=True)
    publication_date = Column(DateTime(timezone=True), server_default=func.now())

    def __str__(self):
        return f"Название {self.title}"
