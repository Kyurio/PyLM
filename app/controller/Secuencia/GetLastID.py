from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia
from app.schemas.SchemaSecuencia import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = Secuencia.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

