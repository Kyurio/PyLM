from pydantic import BaseModel
from datetime import datetime
class UsuarioCreateModel(BaseModel):
    id: int
    id_perfil: str
    nombre: str
    password: str
    correo: str
    estado: bool
    created_at: datetime
    updated_at: datetime

class UsuarioSelectModel(BaseModel):
    id: int
    nombre: str
    created_at: datetime
    updated_at: datetime