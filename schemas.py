from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    is_staff: bool

    class Config:
        orm_mode = True
        # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
