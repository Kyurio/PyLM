from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos
from app.schemas.SchemaConcepto import ConceptoCreateModel

router = APIRouter()

@router.post("/PostConcepto/")
def crear_concepto(request: ConceptoCreateModel):
    try:
        print("respuesta del request concepto", request)
        ususario_data = request.dict()
        concpeto = Conceptos.create(ususario_data)
        return concpeto

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
