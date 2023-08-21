import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import settings

logger = logging.getLogger(__name__)

async_engine = create_async_engine(
    settings.DB_URI,
    pool_pre_ping=True,
    echo=settings.ECHO_SQL,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    future=True,
)


async def get_session() -> AsyncSession:
    try:
        yield async_session
    except SQLAlchemyError as e:
        logger.exception(e)


# FastAPI dependency
DBSession = Annotated[AsyncSession, Depends(get_session)]
