from fastapi import HTTPException, status

access_denied_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
