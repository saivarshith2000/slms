from fastapi import HTTPException, status

from app.models.course import CourseApplicationStatus


def course_not_found_exception(code: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course '{code}' not found")


def course_already_exists_exception(code: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"A Course with code {code} already exists",
    )


def duplicate_application_exception(application_status: CourseApplicationStatus) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"You have already applied for this course. Current status is {application_status}.",
    )
