from fastapi import APIRouter, HTTPException
from app.model.PlanMovimiento import PlanMovimiento
from app.schemas.SchemaPlanMovimineto import PlanMovimientoSelectModel
from typing import List

router = APIRouter()
@router.get("/GetPlanMovimiento/", response_model=List[PlanMovimientoSelectModel])
def listar_plan_movimiento():
    try:

        request = PlanMovimiento.get_all()
        return request

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

