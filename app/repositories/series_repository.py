from sqlalchemy.orm import Session

from app.models import SerieModel
from app.schemas import SerieCreate


def listar_series(db: Session):
    return db.query(SerieModel).all()


def buscar_serie_por_id(db: Session, serie_id: int):
    return (
        db.query(SerieModel)
        .filter(SerieModel.id == serie_id)
        .first()
    )


def cadastrar_serie(db: Session, dados: SerieCreate):
    serie = SerieModel(
        titulo=dados.titulo,
        genero=dados.genero,
        ano_lancamento=dados.ano_lancamento,
        temporadas=dados.temporadas,
        sinopse=dados.sinopse,
    )

    db.add(serie)
    db.commit()
    db.refresh(serie)

    return serie


def atualizar_serie(
    db: Session,
    serie_id: int,
    dados: SerieCreate,
):
    serie = buscar_serie_por_id(db, serie_id)

    if serie is None:
        return None

    serie.titulo = dados.titulo
    serie.genero = dados.genero
    serie.ano_lancamento = dados.ano_lancamento
    serie.temporadas = dados.temporadas
    serie.sinopse = dados.sinopse

    db.commit()
    db.refresh(serie)

    return serie


def excluir_serie(db: Session, serie_id: int):
    serie = buscar_serie_por_id(db, serie_id)

    if serie is None:
        return False

    db.delete(serie)
    db.commit()

    return True