from fastapi import HTTPException, status


def department_not_found_exception(abbr: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Department '{abbr}' not found")
