# app/services/account_service.py
import random

def generate_account_number():
    return "700" + "".join([str(random.randint(0,9)) for _ in range(10)])
