from typing import List

from fastapi import APIRouter

from app.db import AsyncSession

from .schema import DepartmentSchema
from .service import get_all_departments

router = APIRouter(prefix="/departments")


@router.get("/all", response_model=List[DepartmentSchema])
async def get_all_departments_route(async_session: AsyncSession):
    depts = await get_all_departments(async_session)
    print(depts)
    return depts
