from fastapi import APIRouter

from .auth.routes import router as auth_router

router = APIRouter()
router.include_router(auth_router, tags=["auth"])


# TODO: Harden this endpoint
@router.get("health", tags=["health"])
def health():
    return {"message": "Application Healthy!"}
