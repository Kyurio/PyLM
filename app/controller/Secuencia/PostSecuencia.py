from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos
from app.schemas.SchemaConcepto import ConceptoCreateModel

router = APIRouter()
@router.post("/PostConcepto/")
def crear_perfil(request_concepto: ConceptoCreateModel):
    try:
        ususario_data = request_concepto.dict()
        concpeto = Conceptos.create(**ususario_data)
        return {"concepto_id": concpeto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
