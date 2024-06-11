from fastapi import APIRouter, HTTPException
from app.model.DiasRiego import DiasRiego
from app.schemas.SchemaDiasRiego import DiasRiegoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetDiasRiego/", response_model=List[DiasRiegoSelectModel])
def listar_dias_riego():
    try:
        dia = DiasRiego.get_all()
        return dia
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los dias de riego: {str(e)}")

