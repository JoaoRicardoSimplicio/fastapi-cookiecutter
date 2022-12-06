from fastapi import APIRouter


router = APIRouter(
    prefix="/health",
    tags=[],
    dependencies=[],
    responses={500: {"message": "Server Error"}}
)


@router.get("")
async def health():
    return {"message": "ok"}
