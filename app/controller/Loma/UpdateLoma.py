from fastapi import APIRouter, HTTPException
from app.model.Loma import Loma
from app.schemas.SchemaLoma import LomaCreateModel

router = APIRouter()

@router.put("/UpdateLoma/{id}")
def actualizar_loma(id: int, request: LomaCreateModel):
    try:

        response = request.dict()
        success = Loma.update(id, response)
        if success:
            return {"message": "Loma actualizada exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Loma no encontrada")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la loma: {str(e)}")
