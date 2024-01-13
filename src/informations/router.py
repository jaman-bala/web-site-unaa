from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from informations.models import Information
from informations.schemas import InformationOUT, InformationCreate


router = APIRouter()


@router.get("/", response_model=List[InformationOUT])
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    statement = select(Information)
    result = await session.execute(statement)
    information = result.scalars().all()
    return information


@router.post("/", response_model=InformationOUT)
async def add_specific_operations(new_information: InformationCreate, session: AsyncSession = Depends(get_async_session)):
    db_information = Information(**new_information.dict())
    session.add(db_information)
    await session.commit()
    await session.refresh(db_information)
    return db_information
