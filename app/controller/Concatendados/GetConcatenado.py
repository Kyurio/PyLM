from fastapi import APIRouter, HTTPException
from app.model.Concatenados import Concatenados
from app.schemas.SchemaConcatenado import ConcatenadoSelectModel
from typing import List

router = APIRouter()
@router.get("/GetConcatenado/", response_model=List[ConcatenadoSelectModel])
def listar_concatenado():
    try:
        request = Concatenados.get_all()
        return request
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

