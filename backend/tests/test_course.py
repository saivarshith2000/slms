from datetime import date, timedelta

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.course import Course
from app.models.department import Department

departments = [
    Department(name="Department A", code="DEPA", description="Department A's description"),
    Department(name="Department B", code="DEPB", description="Department B's description"),
]

courses = [
    Course(
        name="Course A",
        code="CRSA",
        description="Course A's description",
        credits=4,
        capacity=80,
        department_code="DEPA",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
    ),
    Course(
        name="Course B",
        code="CRSB",
        description="Course B's description",
        credits=2,
        capacity=40,
        department_code="DEPB",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=10),
    ),
]


@pytest.mark.asyncio
async def test_get_all_courses(student_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(Department(**departments[1]))
    await db_session.commit()
    assert 1 == 0


@pytest.mark.asyncio
async def test_create_course(teacher_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0


@pytest.mark.asyncio
async def test_create_course_capacity_reached(teacher_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0


@pytest.mark.asyncio
async def test_apply_to_course(student_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0


@pytest.mark.asyncio
async def test_course_application_status(student_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0


@pytest.mark.asyncio
async def get_pending_course_applications(teacher_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0


@pytest.mark.asyncio
async def test_approve_course_application(teacher_bearer_token: str, client: AsyncClient, db_session: AsyncSession):
    assert 1 == 0
