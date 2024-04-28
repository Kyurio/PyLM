from fastapi import APIRouter, HTTPException
from app.model.PlanMovimiento import PlanMovimiento

router = APIRouter()
@router.delete("/DeletePlanMovimiento/{id}")
def plan_movimineto_delete(id: int):
    try:
        success = PlanMovimiento.delete(id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
