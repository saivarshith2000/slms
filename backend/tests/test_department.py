from datetime import date, timedelta

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.utils import hash_password
from app.models.course import Course
from app.models.department import Department
from app.models.user import Role, User

from .fixtures.users import PASSWORD

departments = [
    {"name": "A Department", "code": "DEPA", "description": "A Department's description"},
    {"name": "B Department", "code": "DEPB", "description": "B Department's description"},
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

courses = [
    {
        "name": "Course A",
        "code": "CRSA",
        "description": "Course A's description",
        "credits": 4,
        "capacity": 80,
        "department_code": "DEPA",
        "start_date": date.today(),
        "end_date": date.today() + timedelta(days=90),
    },
    {
        "name": "Course B",
        "code": "CRSB",
        "description": "Course B's description",
        "credits": 2,
        "capacity": 30,
        "department_code": "DEPA",
        "start_date": date.today(),
        "end_date": date.today() + timedelta(days=30),
    },
]


@pytest.mark.asyncio
async def test_all_departments(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(Department(**departments[1]))
    await db_session.commit()

    response = await client.get("/departments/all")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_department_details(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(User(**users[0]))
    db_session.add(Course(**courses[0]))
    db_session.add(Course(**courses[1]))
    await db_session.commit()

    response = await client.get(f'/departments/{departments[0]["code"]}')
    assert response.status_code == 200
    response = response.json()
    assert response["name"] == departments[0]["name"]
    assert response["code"] == departments[0]["code"]
    assert response["student_count"] == 1
    assert response["course_count"] == 2
