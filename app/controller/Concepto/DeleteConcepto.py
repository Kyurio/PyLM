from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos

router = APIRouter()

@router.delete("/DeleteConcepto/{concepto_id}")
def eliminar_concepto(id: int):

    try:
        success = Conceptos.delete(id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
