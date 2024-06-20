from fastapi import APIRouter, HTTPException
from app.model.InfoRiego import InfoRiego
from app.schemas.SchemaInfoRiego import InfoRiegoCreateModel

router = APIRouter()

@router.post("/PostInfoRiego/")
def crear_info_riego(request: InfoRiegoCreateModel):
    try:
        print("respuesta del request info de riego", request)
        ususario_data = request.dict()
        dia = InfoRiego.create(ususario_data)
        return dia

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear info de riego: {str(e)}")
