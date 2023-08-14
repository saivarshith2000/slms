from typing import Annotated

from jose import JWTError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from .utils import decode_jwt
from .service import get_user_by_email
from .exceptions import credentials_exception, account_inactive_exception

from app.db import AsyncSession
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    async_session: AsyncSession,
) -> User:
    try:
        payload = decode_jwt(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_email(email, async_session)
    if user is None:
        raise credentials_exception
    if not user.active:
        raise account_inactive_exception
    return user
