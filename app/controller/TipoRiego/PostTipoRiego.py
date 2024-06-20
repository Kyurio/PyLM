from fastapi import APIRouter, HTTPException
from app.model.TipoRiego import TipoRiego
from app.schemas.SchemaTipoRiego import TipoRiegoCreateModel

router = APIRouter()

@router.post("/PostTipoRiego/")
def crear_tipo_riego(request: TipoRiegoCreateModel):
    try:
        print("respuesta del request TipoRiego", request)
        ususario_data = request.dict()
        tipo_riego = TipoRiego.create(ususario_data)
        return tipo_riego

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear tipo de riego: {str(e)}")
