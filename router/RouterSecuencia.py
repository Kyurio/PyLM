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

@router.put("/UpdateSecuencia/{id}")
def actualizar_secuencia_route(id: int, request: SecuenciaCreateModel):
    return UpdateSecuencia(id, request)

@router.delete("/DeleteConcepto/{id}")
def eliminar_secuencia_route(id: int):
    return DeleteSecuencia(id)