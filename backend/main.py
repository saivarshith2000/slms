import uvicorn
from app.main import app
from app.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "main:app", reload=settings.RELOAD, port=settings.PORT, workers=settings.WORKERS
    )
