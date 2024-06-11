from fastapi import APIRouter, HTTPException
from app.model.DiasRiego import DiasRiego
from app.schemas.SchemaDiasRiego import DiasRiegoCreateModel

router = APIRouter()

@router.post("/PostDiasRiego/")
def crear_dias_riego(request: DiasRiegoCreateModel):
    try:
        print("respuesta del request dias de riego", request)
        ususario_data = request.dict()
        dia = DiasRiego.create(ususario_data)
        return dia

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear dia de riego: {str(e)}")
