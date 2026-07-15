from sqlalchemy.orm import Session

from app.models import UserModel
from app.repositories.user_repository import (
    buscar_usuario_por_email,
    criar_usuario,
)

from app.schemas.user import (
    UserCreate,
    UserLogin,
)

from app.security import (
    hash_senha,
    verificar_senha,
    criar_access_token,
)


def registrar_usuario(
    db: Session,
    dados: UserCreate,
):

    usuario_existente = buscar_usuario_por_email(
        db,
        dados.email,
    )

    if usuario_existente:
        return None

    usuario = UserModel(
        nome=dados.nome,
        email=dados.email,
        senha_hash=hash_senha(dados.senha),
    )

    return criar_usuario(
        db,
        usuario,
    )


def autenticar_usuario(
    db: Session,
    dados: UserLogin,
):

    usuario = buscar_usuario_por_email(
        db,
        dados.email,
    )

    if usuario is None:
        return None

    if not verificar_senha(
        dados.senha,
        usuario.senha_hash,
    ):
        return None

    token = criar_access_token(
        {
            "sub": usuario.email,
            "user_id": usuario.id,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }