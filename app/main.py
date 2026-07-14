from fastapi import FastAPI

from app.database import criar_tabela
from app.routers.series import router as series_router

app = FastAPI(
    title="Catálogo de Séries",
    version="1.0.0"
)

criar_tabela()

app.include_router(series_router)


@app.get("/")
def home():
    return {
        "mensagem": "API funcionando!"
    }