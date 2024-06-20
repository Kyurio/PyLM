from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()

@router.post("/PostMovimineto/")
def crear_movimiento(request: MovimientoCreateModel):
    try:

        data = request.dict()
        print("esta es la data del congtroller movimiento: ", data)
        response = Movimientos.create(data)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el movimiento: {str(e)}")
