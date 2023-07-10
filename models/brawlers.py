from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database import Base


class Brawler(Base):
    __tablename__ = "brawlers"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer, comment="ID used to query in Brawl Starts API")
    name = Column(String, unique=True, index=True)
    users: Mapped[List["User"]] = relationship(back_populates="favorite_brawler")
