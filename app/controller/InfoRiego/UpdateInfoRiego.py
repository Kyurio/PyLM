from fastapi import APIRouter, HTTPException
from app.model.InfoRiego import InfoRiego
from app.schemas.SchemaInfoRiego import InfoRiegoCreateModel

router = APIRouter()

@router.put("/UpdateInfoRiego/{id}")
def actualizar_info_riego(id: int, request: InfoRiegoCreateModel):
    try:

        response = request.dict()
        success = InfoRiego.update(id, response)
        if success:
            return {"message": "Info de riego actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Info de riego no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el info de riego: {str(e)}")
