from pydantic import BaseModel
from datetime import datetime

class UsuarioResponseModel(BaseModel):

    id_perfil: int
    nombre: str
    password: str
    correo: str
    estado: bool
    created_at: datetime
    updated_at: datetime
