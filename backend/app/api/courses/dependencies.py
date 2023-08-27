from typing import Annotated

from fastapi import Depends

from app.api.auth.dependencies import get_current_user
from app.core.exceptions import access_denied_exception
from app.models.user import Role, User


def check_teacher(user: Annotated[User, Depends(get_current_user)]):
    if not user.role == Role.TEACHER:
        raise access_denied_exception
    return user


def check_student(user: Annotated[User, Depends(get_current_user)]):
    if not user.role == Role.STUDENT:
        raise access_denied_exception

    return user
