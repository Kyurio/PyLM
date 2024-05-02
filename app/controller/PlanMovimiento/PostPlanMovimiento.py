from fastapi import APIRouter, HTTPException
from app.model.PlanMovimiento import PlanMovimiento
from app.schemas.SchemaParametro import ParametroSelectModel

router = APIRouter()
@router.post("/PostPlanMovimiento")
def crear_plan_movimiento(request: ParametroSelectModel):
    try:

        concatenado = request.dict()
        response = PlanMovimiento.create(**concatenado)
        return {"parametro_id": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
