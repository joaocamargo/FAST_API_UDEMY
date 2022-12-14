from email.policy import default
from typing import Optional

from sqlalchemy import PrimaryKeyConstraint
from sqlmodel import Field,SQLModel 


class CursoModel(SQLModel, table=True):
    __tablename__: str = 'cursos'

    id: Optional[int] = Field(default=None,primary_key=True)
    titulo: str
    aulas: int
    horas: int 