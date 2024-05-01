from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos
from app.schemas.SchemaConcepto import ConceptoCreateModel

router = APIRouter()
@router.put("/UpdateConceptos/")
def actualizar_concepto(conceptos_request: ConceptoCreateModel):
    try:
        conceptos_data = conceptos_request.dict()
        success = Conceptos.update(**conceptos_data)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
