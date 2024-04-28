from fastapi import APIRouter
from app.controller.Concatendados import UpdateConcatenado,GetConcatenado,DeleteConcatenado,PostConcatenado
from app.schemas.SchemaConcepto import ConceptoCreateModel, ConceptoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetConcepto/", response_model=List[ConceptoSelectModel])
def listar_concatenado_route():
    return GetConcatenado()

@router.post("/CreateConcepto/")
def crear_concatenado_route(concepto_request: ConceptoCreateModel):
    return PostConcatenado(concepto_request)

@router.put("/UpdateConcepto/")
def actualizar_concatenado_route(concepto_request: ConceptoCreateModel):
    return UpdateConcatenado(concepto_request)

@router.delete("/DeleteConcepto/{perfil_id}")
def eliminar_concatenado_route(concepto_id: int):
    return DeleteConcatenado(concepto_id)