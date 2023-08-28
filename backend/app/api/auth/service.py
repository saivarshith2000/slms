from sqlalchemy import select

from app.api.departments.service import get_department_by_code
from app.db import DBSession
from app.models.user import Role, User

from .exceptions import email_in_use_exception, user_not_found_exception
from .schema import CreateUserSchema
from .utils import hash_password


async def create_user(request: CreateUserSchema, session: DBSession) -> None:
    user_in_db = await session.scalar(select(User).where(User.email == request.email))
    if user_in_db:
        raise email_in_use_exception
    if request.role != Role.ADMIN:
        await get_department_by_code(request.department_code, session)
    user = User(
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        role=request.role,
        department_code=request.department_code,
        password_hash=hash_password(request.password),
        active=False,
    )
    session.add(user)
    await session.commit()


async def get_user_by_email(email: str, session: DBSession) -> User:
    user = await session.scalar(select(User).where(User.email == email))
    if not user:
        raise user_not_found_exception(email)
    return user
