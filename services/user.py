from datetime import datetime

from sqlalchemy.orm import Session

import schemas
from models.users import Brawler, User

# from models.brawlers import Brawler


class UserModelService:
    model = User

    @classmethod
    def get_user(cls, db: Session, user_id: int):
        return db.query(cls.model).filter(cls.model.id == user_id).first()

    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(cls.model).filter(cls.model.email == email).first()

    @classmethod
    def get_users(cls, db: Session, offset: int = 0, limit: int = 100):
        return db.query(cls.model).offset(offset).limit(limit).all()

    @classmethod
    def create_user(cls, db: Session, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = cls.model(email=user.email, hashed_password=fake_hashed_password)
        db_user.registered_on = datetime.now()
        new_brawler = Brawler(name="Shelly")
        db.add(new_brawler)
        db.commit()
        db.refresh(new_brawler)
        db_user.favorite_brawler = new_brawler
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
