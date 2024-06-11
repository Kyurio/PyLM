from fastapi import APIRouter, HTTPException
from app.model.InfoRiego import InfoRiego
from app.schemas.SchemaInfoRiego import InfoRiegoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetInfoRiego/", response_model=List[InfoRiegoSelectModel])
def listar_info_riego():
    try:
        dia = InfoRiego.get_all()
        return dia
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los info de riego: {str(e)}")

