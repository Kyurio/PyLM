from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import ParametroCreateModel

router = APIRouter()

@router.put("/UpdateParametros/{id}")
def actualizar_parametros(id: int, request: ParametroCreateModel):
    try:

        response = request.dict()
        success = Parametros.update(id, response)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
