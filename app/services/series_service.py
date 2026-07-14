from sqlalchemy.orm import Session

from app.schemas import SerieCreate
from app.repositories.series_repository import (
    cadastrar_serie,
    listar_series,
    buscar_serie_por_id,
    atualizar_serie,
    excluir_serie,
)


def criar_serie(db: Session, dados: SerieCreate):
    return cadastrar_serie(db, dados)


def obter_series(db: Session):
    return listar_series(db)


def obter_serie(db: Session, serie_id: int):
    return buscar_serie_por_id(db, serie_id)


def editar_serie(
    db: Session,
    serie_id: int,
    dados: SerieCreate,
):
    return atualizar_serie(db, serie_id, dados)


def remover_serie(db: Session, serie_id: int):
    return excluir_serie(db, serie_id)