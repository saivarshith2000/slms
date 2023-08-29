from fastapi import HTTPException, status


def user_not_found_exception(email: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {email} not found")


account_inactive_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Account not activated yet. Contact your administrator",
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid Credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


email_in_use_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Email already in use",
)
