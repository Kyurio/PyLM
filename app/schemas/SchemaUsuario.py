from pydantic import BaseModel
from datetime import datetime


class UsuarioCreateModel(BaseModel):
    id_perfil: int
    usuario: str
    password: str
    correo: str
    estado: bool


class UsuarioSelectModel(BaseModel):
    id: int
    nombre: str
    created_at: datetime
    updated_at: datetime