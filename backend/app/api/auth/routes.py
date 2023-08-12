from fastapi import APIRouter

router = APIRouter(prefix="/admin")


@router.post("/signup")
def signup_route():
    pass


@router.post("/signin")
def signin_route():
    pass


@router.post("/update-password")
def update_password_route():
    pass


@router.get("/me")
def user_details_route():
    pass
