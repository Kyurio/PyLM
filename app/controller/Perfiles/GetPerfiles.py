from fastapi import HTTPException, APIRouter
from app.model.Perfil import Perfil
from app.schemas.SchemaPerfil import PerfilSelectModel
from typing import List

router = APIRouter()

@router.get("/GetPerfiles/", response_model=List[PerfilSelectModel])
def listar_perfiles():
    try:
        perfiles = Perfil.get_all()
        return perfiles
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los perfiles: {str(e)}")
