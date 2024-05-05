<<<<<<< HEAD
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
=======
from pydantic import BaseModel

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
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449
