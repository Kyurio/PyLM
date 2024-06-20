from fastapi import APIRouter, HTTPException
from app.model.TipoRiego import TipoRiego
from app.schemas.SchemaTipoRiego import TipoRiegoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetTipoRiego/", response_model=List[TipoRiegoSelectModel])
def listar_tipo_riego():
    try:
        tipo_riego = TipoRiego.get_all()
        return tipo_riego
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los tipo de riego: {str(e)}")

