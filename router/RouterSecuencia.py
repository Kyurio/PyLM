from fastapi import APIRouter
from app.controller.Secuencia import GetSecuencia, DeleteSecuencia, UpdateSecuencia, PostSecuencia
from app.schemas.SchemaUsuario import UsuarioResponseModel
from typing import List

router = APIRouter()

@router.get("/GetSecuencia/", response_model=List[UsuarioResponseModel])
def listar_secuencia_route():
    return GetSecuencia()

@router.post("/CreateSecuencia/")
def crear_secuencia_route(request: UsuarioResponseModel):
    return PostSecuencia(request)

@router.put("/UpdateSecuencia/")
def actualizar_secuencia_route(request: UsuarioResponseModel):
    return UpdateSecuencia(request)

@router.delete("/DeleteConcepto/{perfil_id}")
def eliminar_secuencia_route(id: int):
    return DeleteSecuencia(id)