from pydantic import BaseModel
from datetime import datetime

class PerfilCreateModel(BaseModel):
    nombre_perfil: str
    estado: bool
    created: bool
    updated: bool
    deleted: bool
    leer: bool


class PerfilSelectModel(BaseModel):
    id: int
    nombre_perfil: str
    estado: bool
    created_at: datetime
    updated_at: datetime
    created: bool
    updated: bool
    deleted: bool
    leer: bool


