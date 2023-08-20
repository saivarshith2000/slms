import asyncio
import logging

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.main import app
from app.models.base import Base
from app.settings import settings

logger = logging.getLogger(__name__)

# module level fixtures
pytest_plugins = [
    "tests.fixtures.admin",
]


@pytest.fixture(scope="session")
def event_loop():
    # To deal with fastapi and pytest having different scopes for their event loops
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000/api/v1") as client:
        yield client


# drop all database every time when test complete
@pytest_asyncio.fixture(scope="session")
async def async_db_engine():
    async_engine = create_async_engine(
        settings.DB_URI,
        pool_pre_ping=True,
        echo=settings.ECHO_SQL,
    )

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield async_engine

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def db_session(async_db_engine: AsyncEngine) -> AsyncSession:
    async_session = async_sessionmaker(
        bind=async_db_engine,
        expire_on_commit=False,
        autoflush=False,
        future=True,
    )

    async with async_session() as session:
        await session.begin()

        yield session

        await session.rollback()

        for table in reversed(Base.metadata.sorted_tables):
            await session.execute(text(f"TRUNCATE {table.name} CASCADE;"))
            await session.commit()
