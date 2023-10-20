from pydantic import BaseModel, ConfigDict
from uuid import UUID


class UserRead(BaseModel):
    id: UUID
    email: str
    is_superuser: bool
    is_verified: bool

    model_config = ConfigDict(from_attributes=True)


class UserCreat(): 
    id: UUID = None
    email: str
    password: str
    is_superuser: bool = False
    is_verified: bool = False