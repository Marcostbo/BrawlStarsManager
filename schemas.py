from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class FavoriteBrawler(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    is_staff: bool
    favorite_brawler: FavoriteBrawler

    class Config:
        orm_mode = True
        # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
