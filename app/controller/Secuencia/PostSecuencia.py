from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia
from app.schemas.SchemaSecuencia import SecuenciaCreateModel

router = APIRouter()

@router.post("/PostSecuencia/")
def crear_secuencia(data: SecuenciaCreateModel):
    try:

        request = data.dict()
        response = Secuencia.create(request)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el seccuencia: {str(e)}")
