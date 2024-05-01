from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import ParametroSelectModel
from typing import List

router = APIRouter()
@router.get("/GetParametros/", response_model=List[ParametroSelectModel])
def listar_parametros():
    try:

        request = Parametros.get_all()
        return request

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

