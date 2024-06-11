from fastapi import APIRouter, HTTPException
from app.model.InfoRiego import InfoRiego

router = APIRouter()

@router.delete("/DeleteInfoRiego/{info_riego_id}")
def eliminar_info_riego(id: int):

    try:
        success = InfoRiego.delete(id)
        if success:
            return {"message": "Info de riego eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Info de riego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar info de riego: {str(e)}")
