from fastapi import APIRouter
from app.controller.Movimiento import GetMovimiento,PostMovimiento,DeleteMovimiento,UpdateMovimiento
from app.schemas.SchemaMovimiento import MovimientoCreateModel, MovimientoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetMovimiento", response_model=List[MovimientoSelectModel])
def listar_concatenado_route():
    return GetMovimiento()

@router.post("/CreateMovimiento/")
def crear_concatenado_route(response: MovimientoCreateModel):
    return PostMovimiento(response)

@router.put("/UpdateMovimiento/{id}")
def actualizar_concatenado_route(id: int, response: MovimientoCreateModel):
    return UpdateMovimiento(id, response)

@router.delete("/DeleteMovimiento/{concatenado_id}")
def eliminar_perfil_route(request: int):
    return DeleteMovimiento(request)