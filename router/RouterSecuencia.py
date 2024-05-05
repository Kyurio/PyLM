from fastapi import APIRouter
from app.controller.Secuencia import GetSecuencia, DeleteSecuencia, UpdateSecuencia, PostSecuencia
from app.schemas.SchemaSecuencia import SecuenciaSelectModel, SecuenciaCreateModel
from typing import List

router = APIRouter()

@router.get("/GetSecuencia/", response_model=List[SecuenciaSelectModel])
def listar_secuencia_route():
    return GetSecuencia()

@router.post("/CreateSecuencia/")
def crear_secuencia_route(request: SecuenciaCreateModel):
    return PostSecuencia(request)

@router.put("/UpdateSecuencia/")
def actualizar_secuencia_route(request: SecuenciaCreateModel):
    return UpdateSecuencia(request)

@router.delete("/DeleteConcepto/{perfil_id}")
def eliminar_secuencia_route(id: int):
    return DeleteSecuencia(id)