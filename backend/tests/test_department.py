import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.department import Department

departments = [
    {"name": "A Department", "abbreviation": "DEPA", "description": "A Department's description"},
    {"name": "B Department", "abbreviation": "DEPB", "description": "B Department's description"},
]


@pytest.mark.asyncio
async def test_all_departments(client: AsyncClient, db_session: AsyncSession):
    db_session.add(Department(**departments[0]))
    db_session.add(Department(**departments[1]))
    await db_session.commit()

    response = await client.get("/departments/all")
    assert response.status_code == 200
    assert len(response.json()) == 2
