from pydantic import BaseModel

class AccountCreateResponse(BaseModel):
    id: int
    account_number: str
