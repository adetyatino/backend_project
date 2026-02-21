from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_investments():
    return {"message": "Investment list"}
