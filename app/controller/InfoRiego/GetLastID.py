from fastapi import APIRouter, HTTPException
from app.model.InfoRiego import InfoRiego
from app.schemas.SchemaInfoRiego import LastID
from typing import List

router = APIRouter()

@router.get("/GetLastID/", response_model=List[LastID])
def LastID():
    try:
        id = InfoRiego.get_last_id()
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener info de riego: {str(e)}")

