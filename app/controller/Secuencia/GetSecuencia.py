from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia
from app.schemas.SchemaSecuencia import SecuenciaSelectModel
from typing import List

router = APIRouter()

@router.get("/GetSecuencia/", response_model=List[SecuenciaSelectModel])
def listar_secuencia():
    try:

        concepto = Secuencia.get_all()
        return concepto

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

