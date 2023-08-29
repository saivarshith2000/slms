import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.utils import hash_password
from app.models.department import Department
from app.models.user import Role, User

from .fixtures.users import PASSWORD

departments = [
    {"name": "Department A", "code": "DEPA", "description": "Description for Department A"},
    {"name": "Duplicate of Department A", "code": "DEPA", "description": "This is a duplicate"},
]

users = [
    {
        "email": "student-1@slms.com",
        "first_name": "student",
        "last_name": "one",
        "password_hash": hash_password(PASSWORD),
        "role": Role.STUDENT,
        "department_code": departments[0]["code"],
        "active": False,
    },
    {
        "email": "teacher-1@slms.com",
        "first_name": "teacher",
        "last_name": "one",
        "password_hash": hash_password(PASSWORD),
        "role": Role.TEACHER,
        "department_code": departments[0]["code"],
        "active": True,
    },
]


@pytest.mark.asyncio
async def test_expected_signup_flow(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    await db_session.commit()
    signup_data = {
        "email": "student-1@slms.com",
        "first_name": "student",
        "last_name": "one",
        "password": PASSWORD,
        "role": Role.STUDENT,
        "department_code": departments[0]["code"],
    }
    response = await client.post("/auth/signup", json=signup_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_signup_with_duplicate_email(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))
    await db_session.commit()
    signup_data = {
        "email": "student-1@slms.com",
        "first_name": "student",
        "last_name": "one",
        "password": PASSWORD,
        "role": Role.STUDENT,
        "department_code": departments[0]["code"],
    }
    response = await client.post("/auth/signup", json=signup_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already in use"


@pytest.mark.asyncio
async def test_signup_with_invalid_department_code(client: AsyncClient):
    signup_data = {
        "email": "student-1@slms.com",
        "first_name": "student",
        "last_name": "one",
        "password": PASSWORD,
        "role": Role.STUDENT,
        "department_code": departments[0]["code"],
    }
    response = await client.post("/auth/signup", json=signup_data)
    assert response.status_code == 404
    assert response.json()["detail"] == f"Department '{departments[0]['code']}' not found"


@pytest.mark.asyncio
async def test_expected_signin_flow(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[1]))  # must be a active user, or activate before signing in
    await db_session.commit()
    signin_data = {
        "username": users[1]["email"],
        "password": PASSWORD,
    }
    response = await client.post("/auth/signin", data=signin_data)
    assert response.status_code == 200
    response = response.json()
    assert "access_token" in response
    assert "user" in response
    assert response["token_type"] == "bearer"
    assert response["user"]["email"] == users[1]["email"]
    assert response["user"]["first_name"] == users[1]["first_name"]
    assert response["user"]["last_name"] == users[1]["last_name"]
    assert response["user"]["role"] == users[1]["role"]
    assert response["user"]["department_code"] == users[1]["department_code"]


@pytest.mark.asyncio
async def test_inactive_account_signin_flow(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))  # must be an active user, or activate before signing in
    await db_session.commit()
    signin_data = {
        "username": users[0]["email"],
        "password": PASSWORD,
    }
    response = await client.post("/auth/signin", data=signin_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Account not activated yet. Contact your administrator"


@pytest.mark.asyncio
async def test_invalid_email_signin_flow(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    await db_session.commit()
    signin_data = {
        "username": users[0]["email"],
        "password": PASSWORD,
    }
    response = await client.post("/auth/signin", data=signin_data)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_invalid_password_signin_flow(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[1]))  # must be an active user, or activate before signing in
    await db_session.commit()
    signin_data = {
        "username": users[1]["email"],
        "password": "WRONG" + PASSWORD,
    }
    response = await client.post("/auth/signin", data=signin_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Credentials"
