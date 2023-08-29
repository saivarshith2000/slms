from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.db import DBSession
from app.models.user import User

from .dependencies import get_current_user
from .exceptions import account_inactive_exception, credentials_exception
from .schema import BaseUserSchema, CreateUserSchema, SignInResponseSchema
from .service import create_user, get_user_by_email
from .utils import create_jwt, verify_password

router = APIRouter(prefix="/auth")


@router.post("/signup")
async def signup_route(request: CreateUserSchema, session: DBSession):
    await create_user(request, session)
    return {"message": "Sign Up successful. You can sign in once an adminstrator activates your account."}


@router.post("/signin", response_model=SignInResponseSchema)
async def signin_route(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: DBSession,
):
    user = await get_user_by_email(form_data.username, session)
    if not user:
        raise credentials_exception
    if not user.active:
        raise account_inactive_exception
    if not verify_password(form_data.password, user.password_hash):
        raise credentials_exception
    token = create_jwt({"sub": user.email})
    return {"access_token": token, "user": user}


@router.post("/update-password")
def update_password_route():
    pass


@router.get("/me", response_model=BaseUserSchema)
def user_details_route(user: Annotated[User, Depends(get_current_user)]):
    return user
