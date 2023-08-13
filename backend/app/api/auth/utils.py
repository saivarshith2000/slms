from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.settings import settings

context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return context.verify(plain_password, hashed_password)


def create_jwt(data: dict) -> str:
    to_encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRY_MINUTES)
    to_encode.update({"exp": expiry})
    return jwt.encode(
        to_encode.copy(), settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )


def decode_jwt(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
