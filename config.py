from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache


@lru_cache()
def get_settings():
    settings = SensitiveSettings(_env_file=".env", _env_file_encoding="utf-8")
    return settings


class MainSettings(BaseSettings):
    DB_NAME: str = "fastapi-beanie"


class SensitiveSettings(MainSettings):
    MONGO_DB: str = Field(..., env="MONGO_DB")
    DATABASE_TEST_URL: str = Field(..., env="DATABASE_TEST_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

APP_SETTINGS = get_settings()
