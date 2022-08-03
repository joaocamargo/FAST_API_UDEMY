from fileinput import close
from time import clock_getres
from typing import Generator
from sqlalchemy.ext.asyncio.session import AsyncSession
from core.database import Session



async def get_session() -> Generator: 
    session: AsyncSession = Session()

    try: 
        yield session 
    finally:
        await session.close()