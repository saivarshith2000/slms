from typing import List

from sqlalchemy import select

from app.db import DBSession
from app.models.department import Department

from .exception import department_not_found_exception


async def get_all_departments(db_session: DBSession) -> List[Department]:
    async with db_session() as session:
        return await session.scalars(select(Department))


async def get_department_by_abbreviation(abbr: str, db_session: DBSession) -> Department:
    stmt = select(Department).where(Department.abbreviation == abbr)
    async with db_session() as session:
        dept = await session.scalar(stmt)
        if not dept:
            raise department_not_found_exception(abbr)
        return dept
