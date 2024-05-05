from fastapi import APIRouter, HTTPException, Request
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioSelectModel, UsuarioCreateModel

router = APIRouter()

@router.put("/UpdateUsuario/")
def actualizar_usuario(id: int, data: UsuarioCreateModel):
    try:
        usuario_data = data.dict()
        success = Usuarios.update(id, usuario_data)
        return success

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el Usuario: {str(e)}")
