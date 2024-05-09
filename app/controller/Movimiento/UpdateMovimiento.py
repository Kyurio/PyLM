from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()

@router.put("/UpdateMovimiento/{id}")
def actualizar_movimineto(id: int, request: MovimientoCreateModel):
    try:

        conceptos_data = request.dict()
        success = Movimientos.update(id, conceptos_data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
