import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    SECRET_KEY: str
    JWT_EXPIRY_MINUTES: int
    PORT: int = 8000
    WORKERS: int = 1
    RELOAD: bool = False
    ECHO_SQL: bool = False
    ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / f"{os.environ['APP_CONFIG']}.env",
        case_sensitive=True,
    )


settings = Settings.model_validate({})
