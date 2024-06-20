from fastapi import APIRouter, HTTPException
from app.model.Loma import Loma
from app.schemas.SchemaLoma import LomaSelectModel
from typing import List

router = APIRouter()

@router.get("/GetLoma/", response_model=List[LomaSelectModel])
def listar_lomas():
    try:
        loma = Loma.get_all()
        return loma
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las lomas: {str(e)}")

