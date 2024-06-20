from fastapi import APIRouter
from app.controller.Historial import GetHistorial,PostHistorial
from app.schemas.SchemaHistorial import HistorialCreateModel, HistorialSelectModel
from typing import List

router = APIRouter()

@router.get("/GetHistorial", response_model=List[HistorialSelectModel])
def listar_concatenado_route():
    return GetHistorial()

@router.post("/CreateHistorial/")
def crear_concatenado_route(response: HistorialCreateModel):
    return PostHistorial(response)
