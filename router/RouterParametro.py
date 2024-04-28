from fastapi import APIRouter
from app.controller.Parametro import GetParametro,DeleteParametro,PostParametro,UpdateParametro
from app.schemas.SchemaParametro import ParametroCreateModel,ParametroSelectModel
from typing import List
router = APIRouter()

@router.get("/GetParametro/", response_model=List[ParametroSelectModel])
def listar_parametro_route():
    return GetParametro()

@router.post("/CreateParametro/")
def crear_parametro_route(request: ParametroCreateModel):
    return PostParametro(request)

@router.put("/UpdateParametro/")
def actualizar_parametro_route(request: ParametroCreateModel):
    return UpdateParametro(request)

@router.delete("/DeleteParametro/{parametro_id}")
def eliminar_concatenado_route(id: int):
    return DeleteParametro(id)