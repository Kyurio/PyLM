from fastapi import APIRouter
from app.controller.Concepto import PostConcepto,GetConcepto,DeleteConcepto,UpdateConcepto
from app.schemas.SchemaConcepto import ConceptoCreateModel,ConceptoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetConcepto", response_model=List[ConceptoSelectModel])
def listar_concepto_route():
    return GetConcepto()
    
@router.post("/CreateConcepto/")
def crear_concepto_route(concatenado_request: ConceptoCreateModel):
    return PostConcepto(concatenado_request)
    
@router.put("/UpdateConcepto/")
def actualizar_concepto_route(concatenado_router: ConceptoCreateModel):
    return UpdateConcepto(concatenado_router)
    
@router.delete("/DeleteConcepto/{concatenado_id}")
def eliminar_concepto_route(concatenado_id: int):
    return DeleteConcepto(concatenado_id)
