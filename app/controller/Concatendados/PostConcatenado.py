from fastapi import APIRouter, HTTPException
from app.model.Concatenados import Concatenados
from app.schemas.SchemaConcatenado import ConcatenadoCreateModel

router = APIRouter()
@router.post("/PostConcatenado/")
def create_concatenado(request_concepto: ConcatenadoCreateModel):
    try:
        ususario_data = request_concepto.dict()
        concpeto = Conceptos.create(**ususario_data)
        return {"concepto_id": concpeto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")