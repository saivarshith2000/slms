from fastapi import HTTPException, status


def department_not_found_exception(code: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Department '{code}' not found")
