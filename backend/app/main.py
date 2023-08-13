from fastapi import FastAPI
from .api.main import router

app = FastAPI(
    title="SLMS",
    description="A Simple Learning Management System (SLMS)",
    contact={
        "name": "Sai Varshith, Hariyala",
        "email": "varshith.hariyala@honeywell.com",
    },
)

app.include_router(router, prefix="/api/v1")
