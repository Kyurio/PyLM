from fastapi import APIRouter, HTTPException
from app.model.TipoRiego import TipoRiego
from app.schemas.SchemaTipoRiego import TipoRiegoCreateModel

router = APIRouter()

@router.put("/UpdateTipoRiego/{id}")
def actualizar_tipo_riego(id: int, request: TipoRiegoCreateModel):
    try:

        response = request.dict()
        success = TipoRiego.update(id, response)
        if success:
            return {"message": "Tipo de Riego actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Tipo de Riego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el Tipo de Riego: {str(e)}")
