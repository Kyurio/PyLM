from fastapi import APIRouter
from app.controller.Perfiles import PostPerfil, DeletePerfil, UpdatePerfil,GetPerfiles
from app.schemas.SchemaPerfil import PerfilCreateModel, PerfilSelectModel
from typing import List

router = APIRouter()

@router.get("/GetPerfiles/", response_model=List[PerfilSelectModel])
def listar_perfiles_route():
    return GetPerfiles()

@router.post("/CreatePerfiles/")
def crear_perfil_route(perfil_request: PerfilCreateModel):
    return PostPerfil(perfil_request)

@router.put("/UpdatePerfiles/")
def actualizar_perfil_route(perfil_request: PerfilCreateModel):
    return UpdatePerfil(perfil_request)

@router.delete("/DeletePerfiles/{perfil_id}")
def eliminar_perfil_route(perfil_id: int):
    return DeletePerfil(perfil_id)
