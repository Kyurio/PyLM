from fastapi import APIRouter, HTTPException
from app.model.TipoRiego import TipoRiego

router = APIRouter()

@router.delete("/DeleteTipoRiego/{tipo_riego_id}")
def eliminar_tipo_riego(id: int):

    try:
        success = TipoRiego.delete(id)
        if success:
            return {"message": "Tipo Riego eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="TipoRiego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Tipo Riego: {str(e)}")
