from fastapi import APIRouter, HTTPException
from app.model.DiasRiego import DiasRiego
from app.schemas.SchemaDiasRiego import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = DiasRiego.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener dia de riego: {str(e)}")

