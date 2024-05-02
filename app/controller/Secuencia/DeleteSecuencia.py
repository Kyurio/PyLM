from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia

router = APIRouter()

@router.delete("/DeleteSecuencia/{id}")
def eliminar_secuencia(id: int):

    try:
        success = Secuencia.delete(id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
