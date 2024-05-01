from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia
from app.schemas.SchemaSecuencia import SecuenciaCreateModel

router = APIRouter()
@router.put("/UpdateConceptos/")
def actualizar_secuencia(request: SecuenciaCreateModel):
    try:
        data = request.dict()
        success = Secuencia.update(**data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
