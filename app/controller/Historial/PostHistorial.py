from fastapi import APIRouter, HTTPException
from app.model.Historial import Historial
from app.schemas.SchemaHistorial import HistorialCreateModel

router = APIRouter()

@router.post("/PostHistorial/")
def crear_historial(request: HistorialCreateModel):
    try:
        concatenado = request.dict()
        response = Historial.create(**concatenado)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el Historial: {str(e)}")