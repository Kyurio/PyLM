from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioResponseModel

router = APIRouter()

@router.put("/UpdateUsuario/")
def actualizar_usuario(request: UsuarioResponseModel):
    try:

        usuario_data = request.dict()
        success = Usuarios.update(**usuario_data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
