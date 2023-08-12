from fastapi import FastAPI
from api.main import router

app = FastAPI(
    title="SLMS",
    description="A Simple Learning Management System (SLMS)",
    contact={
        "name": "Sai Varshith, Hariyala",
        "email": "varshith.hariyala@honeywell.com",
    },
)

app.include_router(router, prefix="/v1/api")


if __name__ == "__main__":
    import uvicorn
    from settings import settings

    uvicorn.run(
        "main:app", reload=settings.RELOAD, port=settings.PORT, workers=settings.WORKERS
    )
