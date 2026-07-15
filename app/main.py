from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers.series import router as series_router
from app.database import Base
from app.database import engine
from app.models import SerieModel, UserModel
from app.routers import auth

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Catalogo de Series",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")

Base.metadata.create_all(bind=engine)

app.include_router(series_router)
app.include_router(auth.router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )
