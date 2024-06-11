from fastapi import APIRouter, HTTPException
from app.model.Loma import Loma
from app.schemas.SchemaLoma import LomaCreateModel

router = APIRouter()

@router.post("/PostLoma/")
def crear_loma(request: LomaCreateModel):
    try:
        print("respuesta del request loma", request)
        ususario_data = request.dict()
        loma = Loma.create(ususario_data)
        return loma

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear loma: {str(e)}")
