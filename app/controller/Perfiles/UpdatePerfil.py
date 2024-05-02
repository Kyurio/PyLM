from fastapi import HTTPException, APIRouter
from app.model.Perfil import Perfil
from app.schemas.SchemaPerfil import PerfilCreateModel

router = APIRouter()

@router.put("/UpdatePerfil/")
def actualizar_perfil(perfil_request: PerfilCreateModel):
    try:

        perfil_data = perfil_request.dict()
        success = Perfil.update(**perfil_data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
