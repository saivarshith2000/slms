from typing import List

from sqlalchemy import select

from app.models.department import Department
from app.db import AsyncSession

from .exception import department_not_found_exception


async def get_all_departments(async_session: AsyncSession) -> List[Department]:
    async with async_session() as session:
        return await session.scalars(select(Department))


async def get_department_by_abbreviation(abbr: str, async_session: AsyncSession) -> Department:
    stmt = select(Department).where(Department.abbreviation == abbr)
    async with async_session() as session:
        dept = await session.scalar(stmt)
        if not dept:
            raise department_not_found_exception(abbr)
        return dept
