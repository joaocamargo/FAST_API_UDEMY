from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    configuracoes geradas usadas na aplicacao
    """
    API_V1_STR = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:000@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

class config:
    case_sensitive = True


settings = Settings() 