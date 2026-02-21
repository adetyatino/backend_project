from sqlalchemy.orm import Session
from app.models.account import Account

def create_account(db: Session, user_id: int, account_number: str):
    account = Account(user_id=user_id, account_number=account_number)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account
