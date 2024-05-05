from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioResponseModel
from typing import List

router = APIRouter()
@router.get("/GetUsuarios/", response_model=List[UsuarioResponseModel])
def listar_usuarios():
    try:
        user = Usuarios.get_all()
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Usuarios: {str(e)}")

