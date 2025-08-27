import asyncio
import sys
from sqlalchemy import text

from core.database import Base, async_engine, engine, session_fabrik
from core.models import (Room)



if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def get_data():
    async with async_engine.connect() as conn:
        ress = await conn.execute(text("SELECT VERSION()"))
        version = ress.scalar()
        print(f"PostgreSQL Version: {version}")



from sqlalchemy import text
from core.database import engine

def drop_all_tables_force():
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
        conn.commit()
        print("✅ Все таблицы удалены каскадно.")

def create_tables():
    Base.metadata.reflect(engine)
    drop_all_tables_force()

    Base.metadata.create_all(engine)
    
    




