<<<<<<< HEAD
from fastapi import APIRouter
from app.controller.Usuarios import DeleteUsuario, PostUsuario, GetUsuarios, UpdateUsuarios
from app.schemas.SchemaUsuario import UsuarioResponseModel
from typing import List

router = APIRouter()

@router.get("/GetAllUsuarios/", response_model=List[UsuarioResponseModel])
def listar_usuario_route():
    return GetUsuarios()

@router.post("/CreateUsuarios/")
def crear_usuario_route(perfil_request: UsuarioResponseModel):
    return PostUsuario(perfil_request)

@router.put("/UpdateUsuarios/")
def actualizar_usuario_route(perfil_request: UsuarioResponseModel):
    return UpdateUsuarios(perfil_request)

@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_usuario_route(perfil_id: int):
    return DeleteUsuario(perfil_id)
=======
from fastapi import APIRouter, Request
from app.controller.Usuarios import DeleteUsuario, PostUsuario, GetUsuarios, UpdateUsuarios
from app.schemas.SchemaUsuario import UsuarioSelectModel, UsuarioCreateModel
from typing import List

router = APIRouter()


@router.get("/GetAllUsuarios/", response_model=List[UsuarioSelectModel])
def listar_usuario_route():
    return GetUsuarios()


@router.post("/CreateUsuarios/")
def crear_usuario_route(perfil_request: UsuarioCreateModel):
    return PostUsuario(perfil_request)


@router.put("/UpdateUsuario/{usuario_id}")
def actualizar_usuario_route(usuario_id: int, perfil_request: UsuarioCreateModel, request: Request):
    return UpdateUsuarios(usuario_id, perfil_request, request)


@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_usuario_route(perfil_id: int):
    return DeleteUsuario(perfil_id)
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449
