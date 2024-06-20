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
    id_perfil: int
    usuario: str
    password: str
    correo: str
    estado: bool
