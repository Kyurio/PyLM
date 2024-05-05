from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaConcatenado import ConcatenadoCreateModel

router = APIRouter()

@router.post("/PostMovimineto/")
def crear_movimiento(request: ConcatenadoCreateModel):
    try:

        concatenado = request.dict()
        response = Movimientos.create(**concatenado)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
