from sqlalchemy.orm import Session
from app.models import UserModel


def buscar_usuario_por_email(
    db: Session,
    email: str
):
    return (
        db.query(UserModel)
        .filter(UserModel.email == email)
        .first()
    )


def criar_usuario(
    db: Session,
    usuario: UserModel,
):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario