from fastapi import APIRouter

from app.db import DBSession

from .schema import DepartmentDetailSchema, DepartmentSchema
from .service import get_all_departments, get_department_details

router = APIRouter(prefix="/departments")


@router.get("/all", response_model=list[DepartmentSchema])
async def get_all_departments_route(session: DBSession):
    return await get_all_departments(session)


@router.get("/{code}", response_model=DepartmentDetailSchema)
async def get_department_details_route(code: str, session: DBSession):
    return await get_department_details(code, session)
