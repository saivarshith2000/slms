from fastapi import HTTPException, status


def department_already_exists_exception(code: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"A department with code {code} already exists",
    )
