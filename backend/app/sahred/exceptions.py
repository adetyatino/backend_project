from fastapi import HTTPException


class InsufficientFundsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Insufficient funds")


class UnauthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Unauthorized")


class NotFoundException(HTTPException):
    def __init__(self, message="Resource not found"):
        super().__init__(status_code=404, detail=message)
