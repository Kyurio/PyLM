from fastapi import FastAPI, HTTPException, APIRouter
from app.model.Perfil import Perfil
router = APIRouter()
@router.delete("/DeletePerfiles/{perfil_id}")
def eliminar_perfil(perfil_id: int):
    try:
        success = Perfil.delete(perfil_id)
        if success:
            return {"message": "Perfil eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el perfil: {str(e)}")

