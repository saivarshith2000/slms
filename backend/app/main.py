from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.main import router
from .settings import settings

app = FastAPI(
    title="SLMS",
    description="A Simple Learning Management System (SLMS)",
    contact={
        "name": "Sai Varshith, Hariyala",
        "email": "varshith.hariyala@honeywell.com",
    },
)

origins = [
    settings.ALLOWED_ORIGINS,
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
