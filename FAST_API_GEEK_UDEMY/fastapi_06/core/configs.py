from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import List 


class Settings(BaseSettings):
    """
    configuracoes geradas usadas na aplicacao
    """
    API_V1_STR = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:000@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'Q3nYDVivnHTTW2fHaesoUny508eky4uROELfGcs3pTg'
    """"
    import secrets 
    token: str = secrets.token_urlsafe(32) 
    print(token)    
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 #uma semana
    

class config:
    case_sensitive = True


settings: Settings = Settings() 