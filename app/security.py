from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

# Chave secreta (em produção ela ficará em um .env)
SECRET_KEY = "troque-esta-chave-por-uma-chave-segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(
    senha: str,
    senha_hash: str
) -> bool:
    return pwd_context.verify(
        senha,
        senha_hash
    )


def criar_access_token(
    data: dict
) -> str:

    dados = data.copy()

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados.update({"exp": expire})

    return jwt.encode(
        dados,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verificar_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None