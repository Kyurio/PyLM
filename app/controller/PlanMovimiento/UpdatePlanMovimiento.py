from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import ParametroCreateModel

router = APIRouter()

@router.put("/UpdatePlanMovimiento/")
def actualizar_plan_movimiento(request: ParametroCreateModel):
    try:
        response = request.dict()
        success = Parametros.update(**response)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
