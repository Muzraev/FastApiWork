from pydantic import BaseModel

class UserID(BaseModel):
    name: str
    id: int