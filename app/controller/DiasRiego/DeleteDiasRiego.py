from fastapi import APIRouter, HTTPException
from app.model.DiasRiego import DiasRiego

router = APIRouter()

@router.delete("/DeleteDiasRiego/{dias_riego_id}")
def eliminar_dias_riego(id: int):

    try:
        success = DiasRiego.delete(id)
        if success:
            return {"message": "Dia de riego eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Dia de riego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar dia de riego: {str(e)}")
