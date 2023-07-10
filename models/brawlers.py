from typing import List

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, engine


class Brawler(Base):
    __tablename__ = "brawlers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    users: Mapped[List["User"]] = relationship(back_populates="favorite_brawler")


# Base.metadata.create_all(bind=engine)
