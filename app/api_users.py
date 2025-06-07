from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.agent_runner import run_agent

import app
from . import models
from .database import get_db

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/users/{id}")
def read_user(id: int, db: Session = Depends(get_db)):
    return db.query(models.User).filter_by(id=id).first()

class AgentRequest(BaseModel):
    prompt: str

@router.post("/ask-agent/")
def ask_agent(req: AgentRequest):
    response = run_agent(req.prompt)
    return {"response": response}