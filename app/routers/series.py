from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.database import get_db
from app.schemas import Serie, SerieCreate

from app.services.series_service import (
    criar_serie as criar_serie_service,
    obter_series as obter_series_service,
    obter_serie as obter_serie_service,
    editar_serie as editar_serie_service,
    remover_serie as remover_serie_service,
)

router = APIRouter(
    prefix="/series",
    tags=["Séries"]
)


@router.post(
    "",
    response_model=Serie,
    status_code=status.HTTP_201_CREATED
)
def criar_serie(
    serie: SerieCreate,
    db: Session = Depends(get_db),
    usuario = Depends(get_current_user),
):
    return criar_serie_service(db, serie)


@router.get(
    "",
    response_model=list[Serie]
)
def listar_series(
    db: Session = Depends(get_db),
    genero: str | None = None,
    ano_lancamento: int | None = None,
):
    return obter_series_service(db, genero, ano_lancamento)


@router.get(
    "/{serie_id}",
    response_model=Serie
)
def buscar_serie(
    serie_id: int,
    db: Session = Depends(get_db)
):
    serie = obter_serie_service(db, serie_id)

    if serie is None:
        raise HTTPException(
            status_code=404,
            detail="Série não encontrada."
        )

    return serie


@router.put(
    "/{serie_id}",
    response_model=Serie
)
def atualizar_serie(
    serie_id: int,
    dados: SerieCreate,
    db: Session = Depends(get_db),
    usuario = Depends(get_current_user),
):
    serie = editar_serie_service(
        db,
        serie_id,
        dados
    )

    if serie is None:
        raise HTTPException(
            status_code=404,
            detail="Série não encontrada."
        )

    return serie


@router.delete(
    "/{serie_id}"
)
def excluir_serie(
    serie_id: int,
    db: Session = Depends(get_db),
    usuario = Depends(get_current_user),
):
    removida = remover_serie_service(
        db,
        serie_id
    )

    if not removida:
        raise HTTPException(
            status_code=404,
            detail="Série não encontrada."
        )

    return {
        "mensagem": "Série removida com sucesso."
    }