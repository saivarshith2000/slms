from typing import List

from fastapi import APIRouter

from app.db import DBSession

from .schema import DepartmentSchema
from .service import get_all_departments

router = APIRouter(prefix="/departments")


@router.get("/all", response_model=List[DepartmentSchema])
async def get_all_departments_route(db_session: DBSession):
    depts = await get_all_departments(db_session)
    print(depts)
    return depts
