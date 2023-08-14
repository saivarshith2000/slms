from typing import List

from fastapi import APIRouter

from app.db import AsyncSession

from .service import get_all_departments
from .schema import DepartmentSchema

router = APIRouter(prefix="/departments")


@router.get("/all", response_model=List[DepartmentSchema])
async def get_all_departments_route(async_session: AsyncSession):
    depts = await get_all_departments(async_session)
    print(depts)
    return depts
