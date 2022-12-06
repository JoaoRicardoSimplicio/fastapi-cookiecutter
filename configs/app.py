from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    version: str

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings():
    return Settings()
