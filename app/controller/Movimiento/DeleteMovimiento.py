from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos

router = APIRouter()
@router.delete("/DeleteMovimimento/{movimineto_id}")
def movimiento_delete(movimineto_id: int):
    try:
        success = Movimientos.delete(movimineto_id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
