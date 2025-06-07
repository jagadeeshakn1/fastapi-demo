# main.py
import uvicorn
from fastapi import FastAPI
from app.api_users import router as user_router
from app.api_agents import router as agent_router

from app import models, database
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(agent_router)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)