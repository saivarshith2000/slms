from datetime import datetime
from typing import List

from sqlalchemy import select

from app.api.departments.schema import DepartmentSchema
from app.api.departments.service import get_department_by_abbreviation
from app.db import DBSession
from app.models.department import Department
from app.models.user import User

from ..auth.service import get_user_by_email
from .exception import department_already_exists_exception


async def get_all_accounts(db_session: DBSession) -> List[User]:
    async with db_session() as session:
        return await session.scalars(select(User))


async def get_inactive_accounts(db_session: DBSession) -> List[User]:
    async with db_session() as session:
        return await session.scalars(select(User).where(User.active == False))  # noqa


async def activate_account(email: str, dept_abbr: str, db_session: DBSession) -> User:
    user = await get_user_by_email(email, db_session)
    dept = await get_department_by_abbreviation(dept_abbr, db_session)
    async with db_session() as session:
        user.active = True
        user.activated_at = datetime.utcnow()
        user.department_id = dept.id
        session.add(user)
        await session.commit()
        return user


async def deactivate_account(email: str, db_session: DBSession) -> User:
    user = await get_user_by_email(email, db_session)
    async with db_session() as session:
        user.active = False
        user.activated_at = None
        session.add(user)
        await session.commit()
        return user


async def create_department(request: DepartmentSchema, db_session: DBSession) -> Department:
    async with db_session() as session:
        stmt = select(Department).where(Department.abbreviation == request.abbreviation)
        dept_in_db = await session.scalar(stmt)
        if dept_in_db:
            raise department_already_exists_exception(request.abbreviation)

        department = Department(**request.model_dump())
        session.add(department)
        await session.commit()
        return department


async def update_department(abbr: str, request: DepartmentSchema, db_session: DBSession) -> Department:
    dept = await get_department_by_abbreviation(abbr, db_session)
    async with db_session() as session:
        dept.name = request.name
        dept.description = request.description
        session.add(dept)
        await session.commit()
        return dept
