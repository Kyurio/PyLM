from pydantic import BaseModel
from datetime import datetime

class PerfilCreateModel(BaseModel):
    nombre_perfil: str
    descripcion: str
    estado: bool

class PerfilSelectModel(BaseModel):
    id: int
    id_perfil: int
    descripcion: str
    estado: bool
    created_at: datetime
    updated_at: datetime
