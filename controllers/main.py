from fastapi import Depends

from configs.app import (
    app,
    Settings,
    get_settings
)
from controllers import (
    health,
    tasks
)


app.include_router(health.router)
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "version": settings.version
    }
