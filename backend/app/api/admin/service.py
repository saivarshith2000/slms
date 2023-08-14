from typing import List
from datetime import datetime

from sqlalchemy import select

from app.api.departments.schema import DepartmentSchema
from app.api.departments.service import get_department_by_abbreviation

from app.db import AsyncSession
from app.models.user import User
from app.models.department import Department

from app.api.departments.service import get_department_by_abbreviation

from .exception import department_already_exists_exception

from ..auth.service import get_user_by_email


async def get_all_accounts(async_session: AsyncSession) -> List[User]:
    async with async_session() as session:
        return await session.scalars(select(User))


async def get_inactive_accounts(async_session: AsyncSession) -> List[User]:
    async with async_session() as session:
        return await session.scalars(select(User).where(User.active == False))


async def activate_account(
    email: str, dept_abbr: str, async_session: AsyncSession
) -> User:
    user = await get_user_by_email(email, async_session)
    dept = await get_department_by_abbreviation(dept_abbr, async_session)
    async with async_session() as session:
        user.active = True
        user.activated_at = datetime.utcnow()
        user.department_id = dept.id
        session.add(user)
        await session.commit()
        return user


async def deactivate_account(email: str, async_session: AsyncSession) -> User:
    user = await get_user_by_email(email, async_session)
    async with async_session() as session:
        user.active = False
        user.activated_at = None
        session.add(user)
        await session.commit()
        return user


async def create_department(
    request: DepartmentSchema, async_session: AsyncSession
) -> Department:
    async with async_session() as session:
        stmt = select(Department).where(Department.abbreviation == request.abbreviation)
        dept_in_db = await session.scalar(stmt)
        if dept_in_db:
            raise department_already_exists_exception(request.abbreviation)

        department = Department(**request.model_dump())
        session.add(department)
        await session.commit()
        return department


async def update_department(
    abbr: str, request: DepartmentSchema, async_session: AsyncSession
) -> Department:
    dept = await get_department_by_abbreviation(abbr, async_session)
    async with async_session() as session:
        dept.name = request.name
        dept.description = request.description
        session.add(dept)
        await session.commit()
        return dept
