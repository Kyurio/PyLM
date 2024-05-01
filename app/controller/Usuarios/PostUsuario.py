from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioCreateModel

router = APIRouter()

@router.post("/PostUsuario/")
def crear_usuario(request: UsuarioCreateModel):
    try:

        ususario_data = request.dict()
        usuarios = Usuarios.create(**ususario_data)
        return {"perfil_id": usuarios}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
