from fastapi import FastAPI, HTTPException, APIRouter
from app.model.Historial import Historial
from app.schemas.SchemaHistorial import HistorialSelectModel
from typing import List

router = APIRouter()

@router.get("/GetHistorial/", response_model=List[HistorialSelectModel])
def listar_historial():
    try:
        user = Historial.get_all()
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Usuarios: {str(e)}")

