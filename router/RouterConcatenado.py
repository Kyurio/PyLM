from fastapi import APIRouter
from app.controller.Concatendados import UpdateConcatenado, GetConcatenado, DeleteConcatenado, PostConcatenado
from app.schemas.SchemaConcepto import ConceptoCreateModel, ConceptoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetConcepto/", response_model=List[ConceptoSelectModel])
def listar_concatenado_route():
    return GetConcatenado()

@router.post("/CreateConcepto/")
def crear_concatenado_route(request: ConceptoCreateModel):
    return PostConcatenado(request)

@router.put("/UpdateConcepto/{id}")
def actualizar_concatenado_route(id: int, concepto_request: ConceptoCreateModel):
    return UpdateConcatenado(id, concepto_request)

@router.delete("/DeleteConcepto/{id}")
def eliminar_concatenado_route(id: int):
    return DeleteConcatenado(id)