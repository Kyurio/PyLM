from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioResponseModel

router = APIRouter()

@router.post("/PostUsuario/")
def crear_usuario(request: UsuarioResponseModel):
    try:

        print("respuesta de controller: ", request)

        ususario_data = request.dict()
        usuarios = Usuarios.create(**ususario_data)
        return usuarios

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
