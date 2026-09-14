# database.py
from databases import Database
from datetime import datetime
from typing import Optional

POSTGRES_USER = "temp"
POSTGRES_PASSWORD = "temp"
POSTGRES_DB = "advcompro"

database = Database(f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}")

async def connect_db():
    await database.connect()
    print("Database connected")

async def disconnect_db():
    await database.disconnect()
    print("Database disconnected")

async def insert_user(
    username: str,
    password_hash: str,
    email: str,
    token: Optional[str] = None,
    expired_at: Optional[datetime] = None
):
    # Strip timezone info if present, since the DB column is timezone-naive
    if expired_at is not None and expired_at.tzinfo is not None:
        expired_at = expired_at.replace(tzinfo=None)

    query = """
    INSERT INTO users (username, password_hash, email, token, expired_at)
    VALUES (:username, :password_hash, :email, :token, :expired_at)
    RETURNING user_id, username, password_hash, email, token, expired_at, created_at
    """
    values = {
        "username": username,
        "password_hash": password_hash,
        "email": email,
        "token": token,
        "expired_at": expired_at
    }
    return await database.fetch_one(query=query, values=values)

async def get_user(user_id: int):
    query = "SELECT * FROM users WHERE user_id = :user_id"
    return await database.fetch_one(query=query, values={"user_id": user_id})