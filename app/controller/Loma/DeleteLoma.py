from fastapi import APIRouter, HTTPException
from app.model.Loma import Loma

router = APIRouter()

@router.delete("/DeleteLoma/{loma_id}")
def eliminar_loma(id: int):

    try:
        success = Loma.delete(id)
        if success:
            return {"message": "Loma eliminada exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Loma no encontrada")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la loma: {str(e)}")
