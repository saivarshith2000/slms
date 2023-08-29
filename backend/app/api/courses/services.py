from sqlalchemy import and_, select

from app.db import DBSession
from app.models.course import Course, CourseStudent, CourseTeacher, CourseTeacherRole
from app.models.user import User

from .exceptions import course_already_exists_exception, course_not_found_exception, duplicate_application_exception
from .schema import CourseApplicationSchema, CreateCourseSchema


async def get_all_courses(session: DBSession) -> list(Course):
    return await session.scalars(select(Course))


async def create_course(request: CreateCourseSchema, user: User, session: DBSession):
    with session.begin() as txn:
        course = await txn.scalar(select(Course).where(Course.code == request.code))
        if course:
            raise course_already_exists_exception(request.code)
        course = Course(**request.model_dump())
        txn.add(course)
        await txn.commit()
        course_teacher = CourseTeacher(teacher_id=user.id, course_id=course.id, role=CourseTeacherRole.PRIMARY)
        txn.add(course_teacher)
        await txn.commit()


async def apply_to_course(course_code: str, request: CourseApplicationSchema, user: User, session: DBSession):
    with session.begin() as txn:
        course = await txn.scalar(select(Course).where(and_(Course.code == course_code, Course.active == True)))  # noqa
        if course is None:
            raise course_not_found_exception(course_code)
        course_student = await txn.scalar(
            select(CourseStudent).where(
                and_(CourseStudent.student_id == user.id, CourseStudent.course_code == course_code)
            )
        )  # noqa
        if course_student:
            raise duplicate_application_exception(course_student.application_status)

        course_student = CourseStudent(**request.model_dump())
        course_student.student_id = user.id
        course_student.course_code = course_code
        txn.add(course_student)
        await txn.commit()
