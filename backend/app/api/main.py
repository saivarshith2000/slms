from fastapi import APIRouter

from .admin.routes import router as admin_router
from .auth.routes import router as auth_router
from .departments.routes import router as department_router

router = APIRouter()
router.include_router(auth_router, tags=["auth"])
router.include_router(admin_router, tags=["admin"])
router.include_router(department_router, tags=["department"])


# TODO: Harden this endpoint
@router.get("/health", tags=["health"])
def health():
    return {"message": "Healthy"}
