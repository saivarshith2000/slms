import pytest
from httpx import AsyncClient
from sqlalchemy import select
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
async def test_get_all_accounts(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))
    db_session.add(User(**users[1]))
    await db_session.commit()

    response = await client.get("/admin/accounts/all", headers={"Authorization": f"Bearer {admin_bearer_token}"})
    response = response.json()
    assert len(response) == 3  # 2 users and 1 admin


@pytest.mark.asyncio
async def test_get_pending_accounts(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))
    db_session.add(User(**users[1]))
    await db_session.commit()

    response = await client.get("/admin/accounts/pending", headers=headers)
    response = response.json()

    assert len(response) == 1
    assert response[0]["email"] == "student-1@slms.com"


@pytest.mark.asyncio
async def test_activate_user(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))
    await db_session.commit()

    response = await client.post(
        "/admin/accounts/activate",
        json={"email": users[0]["email"]},
        headers=headers,
    )
    assert response.status_code == 200

    user = await db_session.scalar(select(User).where(User.email == users[0]["email"]))
    assert user.active is True

    department = await db_session.scalar(select(Department).where(Department.code == departments[0]["code"]))
    assert user.department_code == department.code


@pytest.mark.asyncio
async def test_deactivate_user(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[1]))
    await db_session.commit()

    response = await client.post("/admin/accounts/deactivate", params={"email": users[1]["email"]}, headers=headers)
    assert response.status_code == 200

    user = await db_session.scalar(select(User).where(User.email == users[1]["email"]))
    assert user.active is False


@pytest.mark.asyncio
async def test_create_department(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}

    response = await client.post("/admin/departments/create", headers=headers, json=departments[0])
    assert response.status_code == 200

    department = await db_session.scalar(select(Department).where(Department.code == departments[0]["code"]))
    assert department is not None


@pytest.mark.asyncio
async def test_create_department_prevent_duplicate(
    admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession
):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}
    db_session.add(Department(**departments[0]))
    await db_session.commit()

    response = await client.post("/admin/departments/create", headers=headers, json=departments[0])
    assert response.status_code == 400
    assert departments[0]["code"] in response.json()["detail"]


@pytest.mark.asyncio
async def test_update_department(admin_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    headers = {"Authorization": f"Bearer {admin_bearer_token}"}
    db_session.add(Department(**departments[0]))
    await db_session.commit()

    data = {"name": "Updated Department of Pytest", "description": "Updated description of this department"}
    response = await client.put(f"/admin/departments/update/{departments[0]['code']}", headers=headers, json=data)
    assert response.status_code == 200

    department = await db_session.scalar(select(Department).where(Department.code == departments[0]["code"]))
    assert department.name == data["name"]
    assert department.description == data["description"]
