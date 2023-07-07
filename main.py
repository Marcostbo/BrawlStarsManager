from fastapi import FastAPI
import models
from database import engine
from routes import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Brawl Stars Manager"}
