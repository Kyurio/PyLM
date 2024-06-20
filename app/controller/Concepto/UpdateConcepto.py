from fastapi import APIRouter, HTTPException
from app.model.Conceptos import Conceptos
from app.schemas.SchemaConcepto import ConceptoCreateModel

router = APIRouter()

@router.put("/UpdateConceptos/{id}")
def actualizar_concepto(id: int, request: ConceptoCreateModel):
    try:

        response = request.dict()
        success = Conceptos.update(id, response)
        if success:
            return {"message": "Perfil actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil: {str(e)}")
