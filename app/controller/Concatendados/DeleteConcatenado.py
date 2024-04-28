from fastapi import APIRouter, HTTPException
from app.model.Concatenados import Concatenados

router = APIRouter()
@router.delete("/DeleteConcatenado/{concatenado_id}")
def eliminar_concatenado(concatenado_id: int):
    try:
        success = Concatenados.delete(concatenado_id)
        if success:
            return {"message": "Conceptos eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Conceptos no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Conceptos: {str(e)}")
