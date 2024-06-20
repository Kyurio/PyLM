from fastapi import APIRouter
from app.controller.Concepto import PostConcepto,GetConcepto,DeleteConcepto,UpdateConcepto
from app.schemas.SchemaConcepto import ConceptoCreateModel,ConceptoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetConcepto", response_model=List[ConceptoSelectModel])
def listar_concepto_route():
    return GetConcepto()
    
@router.post("/CreateConcepto/")
def crear_concepto_route(request: ConceptoCreateModel):
    return PostConcepto(request)
    
@router.put("/UpdateConcepto/{id}")
def actualizar_concepto_route(id: int, request: ConceptoCreateModel):
    return UpdateConcepto(id, request)
    
@router.delete("/DeleteConcepto/{id}")
def eliminar_concepto_route(id: int):
    return DeleteConcepto(id)
