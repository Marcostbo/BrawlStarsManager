# from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base, engine
#
# from typing import List
#
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
#
#
# class Brawler(Base):
#     __tablename__ = "brawlers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     users: Mapped[List["User"]] = relationship(back_populates="favorite_brawler")
#
#
# Base.metadata.create_all(bind=engine)
