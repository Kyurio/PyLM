from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()
@router.put("/UpdateMovimiento/")
def actualizar_movimineto(request: MovimientoCreateModel):
    try:
        conceptos_data = request.dict()
        success = Movimientos.update(**conceptos_data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
