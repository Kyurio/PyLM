from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios

router = APIRouter()

@router.delete("/DeleteUsuarios/{id}")
def eliminar_usuario(id: int):
    try:
        success = Usuarios.delete(id)
        if success:
            return {"message": "Usuario eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {str(e)}")
