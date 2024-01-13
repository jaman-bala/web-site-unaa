from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from database import get_async_session
from .schemas import NewsBase, NewsCreate
from .models import News


router = APIRouter()


@router.get("/", response_model=List[NewsBase])
async def get_news(session: AsyncSession = Depends(get_async_session)):
    statement = select(News)
    result = await session.execute(statement)
    news = result.scalars().all()
    return news


@router.post("/", response_model=NewsBase)
async def create_news(news_create: NewsCreate, session: AsyncSession = Depends(get_async_session)):
    news = News(**news_create.dict())
    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news
