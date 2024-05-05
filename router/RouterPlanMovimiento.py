from fastapi import APIRouter
from app.controller.PlanMovimiento import PostPlanMovimiento, GetPlanMovimiento, UpdatePlanMovimiento, DeletePlanMovimineto
from app.schemas.SchemaPlanMovimineto import PlanMovimientoCreateModel, PlanMovimientoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetPlanMovimiento/", response_model=List[PlanMovimientoSelectModel])
def listar_pla_movimiento_route():
    return GetPlanMovimiento()

@router.post("/CreatePlanMovimiento/")
def crear_pla_movimiento_route(request: PlanMovimientoCreateModel):
    return PostPlanMovimiento(request)

@router.put("/UpdatePlanMovimiento/")
def actualizar_pla_movimiento_route(request: PlanMovimientoCreateModel):
    return UpdatePlanMovimiento(request)

@router.delete("/DeleteConcepto/{perfil_id}")
def eliminar_pla_movimiento_route(id: int):
    return DeletePlanMovimineto(id)