from typing import Annotated

from fastapi import Depends

from app.models.user import User, Role

from ..auth.dependencies import get_current_user

from .exception import access_denied_exception


def is_admin(user: Annotated[User, Depends(get_current_user)]):
    if not user.role == Role.ADMIN:
        raise access_denied_exception
