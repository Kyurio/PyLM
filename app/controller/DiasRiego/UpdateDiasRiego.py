from fastapi import APIRouter, HTTPException
from app.model.DiasRiego import DiasRiego
from app.schemas.SchemaDiasRiego import DiasRiegoCreateModel

router = APIRouter()

@router.put("/UpdateDiasRiego/{id}")
def actualizar_dias_riego(id: int, request: DiasRiegoCreateModel):
    try:

        response = request.dict()
        success = DiasRiego.update(id, response)
        if success:
            return {"message": "Dia de riego actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Dia de riego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el dia de riego: {str(e)}")
