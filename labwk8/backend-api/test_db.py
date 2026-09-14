# test_db.py
from databases import Database
import asyncio

POSTGRES_USER = "temp"
POSTGRES_PASSWORD = "temp"
POSTGRES_DB = "advcompro"

database = Database(f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}")

async def main():
    await database.connect()
    print("Database connected successfully!")

    query = "SELECT current_database(), current_user;"
    result = await database.fetch_one(query=query)
    print(f"Connected to DB: {result[0]} as User: {result[1]}")

    await database.disconnect()
    print("Database disconnected.")

if __name__ == "__main__":
    asyncio.run(main())