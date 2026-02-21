import random
from datetime import datetime, timedelta
from app.models.otp import OTP

def generate_otp():
    return str(random.randint(100000, 999999))

def create_otp(db, user_id: int):
    code = generate_otp()
    otp = OTP(
        user_id=user_id,
        code=code,
        expires_at=datetime.utcnow() + timedelta(minutes=5)
    )
    db.add(otp)
    db.commit()
    return code
