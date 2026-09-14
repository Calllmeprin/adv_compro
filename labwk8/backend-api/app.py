# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import database  # Import our new database layer

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    password_hash: str
    email: str
    token: Optional[str] = None
    expired_at: Optional[datetime] = None

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    token: Optional[str] = None
    expired_at: Optional[datetime] = None
    created_at: datetime

@app.on_event("startup")
async def startup():
    await database.connect_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect_db()

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    result = await database.insert_user(
        user.username,
        user.password_hash,
        user.email,
        user.token,
        user.expired_at
    )
    if result is None:
        raise HTTPException(status_code=400, detail="Error creating user")
    return dict(result)

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    result = await database.get_user(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(result)