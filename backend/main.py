from app.core.log import log_config
from app.main import app

import uvicorn

from app.settings import settings


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.RELOAD,
        port=settings.PORT,
        workers=settings.WORKERS,
        log_config=log_config,
    )
