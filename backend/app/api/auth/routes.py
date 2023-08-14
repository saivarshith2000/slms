from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User
from app.db import AsyncSession

from .schema import BaseUserSchema, CreateUserSchema
from .dependencies import get_current_user
from .utils import create_jwt, verify_password
from .service import get_user_by_email, create_user
from .exceptions import credentials_exception, account_inactive_exception

router = APIRouter(prefix="/auth")


@router.post("/signup")
async def signup_route(request: CreateUserSchema, async_session: AsyncSession):
    await create_user(request, async_session)
    return {
        "message": "Sign Up successful. You can sign in once an adminstrator activates your account."
    }


@router.post("/signin")
async def signin_route(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    async_session: AsyncSession,
):
    user = await get_user_by_email(form_data.username, async_session)
    if not user:
        raise credentials_exception
    if not user.active:
        raise account_inactive_exception
    if not verify_password(form_data.password, user.password_hash):
        raise credentials_exception
    token = create_jwt({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/update-password")
def update_password_route():
    pass


@router.get("/me", response_model=BaseUserSchema)
def user_details_route(user: Annotated[User, Depends(get_current_user)]):
    return user