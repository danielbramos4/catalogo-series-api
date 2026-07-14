from pydantic import BaseModel, Field, ConfigDict


class SerieCreate(BaseModel):
    titulo: str = Field(..., min_length=1)
    genero: str = Field(..., min_length=1)
    ano_lancamento: int = Field(..., ge=1900)
    temporadas: int = Field(..., ge=1)
    sinopse: str = Field(..., min_length=1)


class Serie(SerieCreate):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )