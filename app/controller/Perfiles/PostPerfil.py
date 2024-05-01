from fastapi import HTTPException, APIRouter
from app.model.Perfil import Perfil
from app.schemas.SchemaPerfil import PerfilCreateModel

router = APIRouter()

@router.post("/PostPerfiles/")
def crear_perfil(perfil_request: PerfilCreateModel):
    try:
        perfil_data = perfil_request.dict()
        response = Perfil.create(**perfil_data)
        if response is not None:  # Verifica si la respuesta no es None
            return {"status": "Success"}, 200
        else:  # Si la respuesta es None, significa que el insert falló
            raise HTTPException(status_code=500, detail="Error al crear el perfil")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
