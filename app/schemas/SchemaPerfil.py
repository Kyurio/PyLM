from pydantic import BaseModel
from datetime import datetime

class PerfilCreateModel(BaseModel):
    nombre_perfil: str
    created: int
    updated: int
    deleted: int
    leer: int
    estado: bool

class PerfilSelectModel(BaseModel):
    id: int
    nombre_perfil: str
    created: int
    updated: int
    deleted: int
    leer: int
    estado: bool
    created_at: datetime
    updated_at: datetime
