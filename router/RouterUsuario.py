
from fastapi import APIRouter
from app.controller.Usuarios import DeleteUsuario, PostUsuario, GetUsuarios, UpdateUsuarios
from app.schemas.SchemaUsuario import UsuarioSelectModel, UsuarioCreateModel
from typing import List

router = APIRouter()

@router.get("/GetAllUsuarios/", response_model=List[UsuarioSelectModel])
def listar_usuario_route():
    return GetUsuarios()

@router.post("/CreateUsuarios/")
def crear_usuario_route(request: UsuarioCreateModel):
    return PostUsuario(request)

@router.put("/UpdateUsuarios/{id}")
def actualizar_usuario_route(id: int, request: UsuarioCreateModel):
    return UpdateUsuarios(id, request)

@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_usuario_route(id: int):
    return DeleteUsuario(id)