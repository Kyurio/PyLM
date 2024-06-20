from fastapi import APIRouter, HTTPException
from app.model.Movimineto import Movimientos
from app.schemas.SchemaMovimiento import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = Movimientos.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

