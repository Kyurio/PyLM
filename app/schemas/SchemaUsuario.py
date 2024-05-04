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