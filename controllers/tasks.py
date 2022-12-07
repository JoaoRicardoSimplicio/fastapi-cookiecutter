from fastapi import (
    APIRouter,
    Body
)
from fastapi.responses import JSONResponse

from worker.tasks import create_task


router = APIRouter(
    prefix="/tasks",
    tags=[],
    dependencies=[],
    responses={500: {"message": "Server Error"}}
)


@router.post("", status_code=201)
async def run_task(payload = Body(...)):
    task_type = payload["type"]
    task = create_task.delay(task_type)
    return JSONResponse({"task_id": task.id})
