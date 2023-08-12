import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    PORT: int
    WORKERS: int
    RELOAD: bool
    ECHO_SQL: bool

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / f"{os.environ['APP_CONFIG']}.env",
        case_sensitive=True,
    )


settings = Settings.model_validate({})
