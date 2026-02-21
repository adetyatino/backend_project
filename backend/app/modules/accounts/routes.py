from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.utils.account_number import generate_account_number
from app.repositories.account_repo import create_account

router = APIRouter()

@router.post("/")
def create_new_account(user_id: int, db: Session = Depends(get_db)):
    account_number = generate_account_number()
    account = create_account(db, user_id, account_number)
    return account
