from fastapi import APIRouter, HTTPException
from app.model.PlanMovimiento import PlanMovimiento
from app.schemas.SchemaPlanMovimineto import PlanMovimientoCreateModel

router = APIRouter()
@router.post("/PostPlanMovimiento")
def crear_plan_movimiento(request: PlanMovimientoCreateModel):
    try:

        data = request.dict()
        response = PlanMovimiento.create(data)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
