from typing import List

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    registered_on = Column(DateTime)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)

    favorite_brawler_id: Mapped[int] = mapped_column(ForeignKey("brawlers.id"))
    favorite_brawler: Mapped["Brawler"] = relationship(back_populates="users")


# class Brawler(Base):
#     __tablename__ = "brawlers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     users: Mapped[List["User"]] = relationship(back_populates="favorite_brawler")


# Base.metadata.create_all(bind=engine)
