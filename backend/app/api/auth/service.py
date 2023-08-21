from sqlalchemy import select

from app.db import DBSession
from app.models.user import User

from .exceptions import email_in_use_exception, user_not_found_exception
from .schema import CreateUserSchema
from .utils import hash_password


async def create_user(request: CreateUserSchema, db_session: DBSession) -> None:
    async with db_session() as session:
        user_in_db = await session.scalar(select(User).where(User.email == request.email))
        if user_in_db:
            raise email_in_use_exception
        user = User(
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            role=request.role,
            password_hash=hash_password(request.password),
        )
        session.add(user)
        await session.commit()


async def get_user_by_email(email: str, db_session: DBSession) -> User:
    async with db_session() as session:
        user = await session.scalar(select(User).where(User.email == email))
        if not user:
            raise user_not_found_exception(email)
        return user
