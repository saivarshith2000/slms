from typing import Annotated

from fastapi import Depends

from app.api.auth.dependencies import get_current_user
from app.core.exceptions import access_denied_exception
from app.models.user import Role, User


def is_admin(user: Annotated[User, Depends(get_current_user)]):
    if not user.role == Role.ADMIN:
        raise access_denied_exception
