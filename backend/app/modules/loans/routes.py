from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_loans():
    return {"message": "Loan list"}
