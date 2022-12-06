from fastapi import (
    Depends,
    FastAPI
)

from configs.app import (
    Settings,
    get_settings
)
from controllers import health


app = FastAPI(title=get_settings().app_name)
app.include_router(health.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "version": settings.version
    }
