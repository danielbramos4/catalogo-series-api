from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class SerieModel(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String, nullable=False)

    genero = Column(String, nullable=False)

    ano_lancamento = Column(Integer, nullable=False)

    temporadas = Column(Integer, nullable=False)

    sinopse = Column(String, nullable=False)