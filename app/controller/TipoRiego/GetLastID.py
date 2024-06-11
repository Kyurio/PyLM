from fastapi import APIRouter, HTTPException
from app.model.TipoRiego import TipoRiego
from app.schemas.SchemaTipoRiego import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = TipoRiego.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el Tipo Riego: {str(e)}")

