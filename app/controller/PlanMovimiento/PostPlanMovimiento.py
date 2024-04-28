from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import ParametroSelectModel

router = APIRouter()
@router.post("/PostPlanMovimiento")
def crear_plan_movimiento(request: ParametroSelectModel):
    try:
        concatenado = request.dict()
        response = Parametros.create(**concatenado)
        return {"parametro_id": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
