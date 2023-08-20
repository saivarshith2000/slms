from typing import AsyncIterator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.utils import hash_password
from app.models.user import Role, User

ADMIN_PASSWORD = "password"
ADMIN_EMAIL = "admin@slms.com"


@pytest_asyncio.fixture()
async def admin_bearer_token(db_session: AsyncSession, client: AsyncIterator) -> str:
    # Login as admin and get bearer token
    admin = User(
        first_name="Admin",
        last_name="User",
        email=ADMIN_EMAIL,
        password_hash=hash_password(ADMIN_PASSWORD),
        role=Role.ADMIN,
        active=True,
    )
    db_session.add(admin)
    await db_session.commit()

    response = await client.post("/auth/signin", data={"username": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
    return response.json()["access_token"]
