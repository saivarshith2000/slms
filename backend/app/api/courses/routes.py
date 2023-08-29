from fastapi import APIRouter

from app.db import DBSession

from .dependencies import check_student, check_teacher
from .schema import CourseApplicationSchema, CreateCourseSchema
from .services import apply_to_course, create_course, get_all_courses

router = APIRouter(prefix="/courses")


@router.get("/all")
async def get_all_department_route(session: DBSession):
    return await get_all_courses(session)


@router.get("/create")
async def create_course_route(request: CreateCourseSchema, user: check_teacher, session: DBSession):
    await create_course(request, user, session)


@router.post("/{course_code}/apply")
async def apply_to_course_route(
    course_code: str, request: CourseApplicationSchema, user: check_student, session: DBSession
):
    raise apply_to_course(course_code, request, user, session)


@router.get("/{course_code}/applications/pending")
async def get_pending_applications_route(session: DBSession):
    raise NotImplementedError


@router.get("/{course_code}/application/{application_id}/status")
async def get_course_application_status_route(session: DBSession):
    raise NotImplementedError
