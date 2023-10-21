from pydantic import BaseModel, ConfigDict
from uuid import UUID


class UserRead(BaseModel):
    id: UUID
    telegramm_id: str
    email: str
    is_superuser: bool
    is_verified: bool 

    model_config = ConfigDict(from_attributes=True)


class UserCreat(BaseModel): 
    id: UUID = None
    telegramm_id: str
    email: str
    password: str
    is_superuser: bool = False
    is_verified: bool = False

