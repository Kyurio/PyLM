from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos
from app.schemas.SchemaConcepto import ConceptoSelectModel
from typing import List

router = APIRouter()

@router.get("/GetConcepto/", response_model=List[ConceptoSelectModel])
def listar_conceptos():
    try:
        concepto = Conceptos.get_all()
        return concepto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

