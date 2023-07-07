from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import schemas
from dependencies import get_db
from services.user import UserModelService

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = UserModelService.get_user_by_email(
        db=db,
        email=user.email
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserModelService.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserModelService.get_users(
        db=db,
        offset=offset,
        limit=limit
    )
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserModelService.get_user(
        db=db,
        user_id=user_id
    )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
