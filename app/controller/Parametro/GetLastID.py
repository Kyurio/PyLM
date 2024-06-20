from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = Parametros.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

