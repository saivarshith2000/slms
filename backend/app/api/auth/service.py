from sqlalchemy import select

from app.db import AsyncSession
from app.models.user import User

from .schema import CreateUserSchema
from .utils import hash_password
from .exceptions import email_in_user_exception


async def create_user(request: CreateUserSchema, async_session: AsyncSession) -> None:
    async with async_session() as session:
        user_in_db = await session.scalar(
            select(User).where(User.email == request.email)
        )
        if user_in_db:
            raise email_in_user_exception
        user = User(
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            role=request.role,
            password_hash=hash_password(request.password),
        )
        session.add(user)
        await session.commit()


async def get_user_by_email(email: str, async_session: AsyncSession) -> User:
    async with async_session() as session:
        return await session.scalar(select(User).where(User.email == email))
