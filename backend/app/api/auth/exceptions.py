from fastapi import HTTPException, status

account_inactive_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Account not activated yet. Contact your administrator",
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


email_in_user_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Email already in use",
)
