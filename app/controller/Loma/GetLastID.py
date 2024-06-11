from fastapi import APIRouter, HTTPException
from app.model.Loma import Loma
from app.schemas.SchemaLoma import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = Loma.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la Loma: {str(e)}")

