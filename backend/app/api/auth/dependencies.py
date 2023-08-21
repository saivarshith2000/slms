from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.db import DBSession
from app.models.user import User

from .exceptions import account_inactive_exception, credentials_exception
from .service import get_user_by_email
from .utils import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db_session: DBSession,
) -> User:
    try:
        payload = decode_jwt(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_email(email, db_session)
    if user is None:
        raise credentials_exception
    if not user.active:
        raise account_inactive_exception
    return user
