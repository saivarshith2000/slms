from typing import List

from sqlalchemy import select

from app.db import DBSession
from app.models.department import Department

from .exception import department_not_found_exception


async def get_all_departments(session: DBSession) -> List[Department]:
    return await session.scalars(select(Department))


async def get_department_by_code(code: str, session: DBSession) -> Department:
    dept = await session.scalar(select(Department).where(Department.code == code))
    if not dept:
        raise department_not_found_exception(code)
    return dept
