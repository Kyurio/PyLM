from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros

router = APIRouter()
@router.delete("/DeleteParametro/{id}")
def parametro_delete(id: int):
    try:
        success = Parametros.delete(id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
