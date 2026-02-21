from passlib.context import CryptContext
from app.repositories.user_repo import get_user_by_email, create_user
from app.core.security import create_access_token
from app.core.exceptions import UnauthorizedException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db, email, password):
    hashed = pwd_context.hash(password)
    return create_user(db, email, hashed)

def authenticate_user(db, email, password):
    user = get_user_by_email(db, email)
    if not user or not pwd_context.verify(password, user.password_hash):
        raise UnauthorizedException("Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return token
