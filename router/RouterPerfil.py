from fastapi import APIRouter
from app.controller.Perfiles import PostPerfil, DeletePerfil, UpdatePerfil,GetPerfiles
from app.schemas.SchemaPerfil import PerfilCreateModel, PerfilSelectModel
from typing import List

router = APIRouter()

@router.get("/GetPerfiles/", response_model=List[PerfilSelectModel])
def listar_perfiles_route():
    return GetPerfiles()

@router.post("/CreatePerfiles/")
def crear_perfil_route(request: PerfilCreateModel):
    return PostPerfil(request)

@router.put("/UpdatePerfiles/{id}")
def actualizar_perfil_route(id: int, request: PerfilCreateModel):
    return UpdatePerfil(id, request)

@router.delete("/DeletePerfiles/{perfil_id}")
def eliminar_perfil_route(id: int):
    return DeletePerfil(id)
