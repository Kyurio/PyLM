from fastapi import APIRouter, HTTPException
from app.model.Concatenados import Concatenados
from app.schemas.SchemaConcatenado import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = Conceptos.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

