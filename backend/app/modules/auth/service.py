from sqlalchemy.orm import Session
from app.models.user import User
from app.models.wallet import Wallet
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, data):
    user = User(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    wallet = Wallet(user_id=user.id, balance=0)
    db.add(wallet)
    db.commit()

    return user


def login_user(db: Session, data):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        return None

    token = create_access_token({"sub": str(user.id)})
    return token
