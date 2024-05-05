from fastapi import APIRouter, HTTPException
from app.model.Parametros import Parametros
from app.schemas.SchemaParametro import ParametroSelectModel

router = APIRouter()
@router.post("/PostParametro")
def crear_parametros(data: ParametroSelectModel):
    try:

        request = data.dict()
        response = Parametros.create(request)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el seccuencia: {str(e)}")
