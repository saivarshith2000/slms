from sqlalchemy import and_, func, select

from app.db import DBSession
from app.models.course import Course
from app.models.department import Department
from app.models.user import Role, User

from .exceptions import department_not_found_exception
from .schema import DepartmentDetailSchema, DepartmentSchema


async def get_all_departments(session: DBSession) -> list[DepartmentSchema]:
    return await session.scalars(select(Department))


async def get_department_by_code(code: str, session: DBSession) -> Department:
    dept = await session.scalar(select(Department).where(Department.code == code))
    if not dept:
        raise department_not_found_exception(code)
    return dept


async def get_department_details(code: str, session: DBSession) -> DepartmentDetailSchema:
    dept = await get_department_by_code(code, session)
    student_count = await session.scalar(
        select(func.count()).select_from(User).where(and_(User.department_code == dept.code, User.role == Role.STUDENT))
    )
    course_count = await session.scalar(
        select(func.count()).select_from(Course).where(Course.department_code == dept.code)
    )
    return DepartmentDetailSchema(
        **dept.__dict__,
        student_count=student_count,
        course_count=course_count,
    )
