from fastapi import APIRouter, HTTPException
from app.model.Secuencia import Secuencia
from app.schemas.SchemaSecuencia import SecuenciaCreateModel

router = APIRouter()

@router.post("/PostSecuencia/")
def crear_secuencia(request: SecuenciaCreateModel):
    try:

        ususario_data = request.dict()
        concpeto = Secuencia.create(**ususario_data)
        return {"concepto_id": concpeto}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
