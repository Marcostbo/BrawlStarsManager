from database import Base, engine

from .brawlers import Brawler
from .users import User

Base.metadata.create_all(bind=engine)

