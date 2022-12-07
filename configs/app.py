from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from pydantic import BaseSettings

from configs.database import SessionLocal


class Settings(BaseSettings):
    app_name: str
    version: str

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings():
    return Settings()


app = FastAPI(title=get_settings().app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
