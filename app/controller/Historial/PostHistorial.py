from fastapi import APIRouter, HTTPException
from app.model.Historial import Historial
from app.schemas.SchemaConcatenado import ConcatenadoCreateModel

router = APIRouter()


@router.post("/PostHistorial/")
def crear_historial(request: ConcatenadoCreateModel):
    try:
        concatenado = request.dict()
        response = Historial.create(**concatenado)
        return {"Historial_id": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el Historial: {str(e)}")