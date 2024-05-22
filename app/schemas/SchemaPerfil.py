from pydantic import BaseModel
from datetime import datetime

class PerfilCreateModel(BaseModel):
    nombre_perfil: str
    estado: bool
    created: int
    updated: int
    deleted: int
    leer: int


class PerfilSelectModel(BaseModel):
    id: int
    nombre_perfil: str
    estado: bool
    created_at: datetime
    updated_at: datetime
    created: int
    updated: int
    deleted: int
    leer: int


