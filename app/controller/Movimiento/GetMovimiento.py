from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaMovimiento import MovimientoSelectModel
from typing import List

router = APIRouter()
@router.get("/GetMovimineto/", response_model=List[MovimientoSelectModel])
def listar_movimineto():
    try:
        request = Movimientos.get_all()
        return request
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

