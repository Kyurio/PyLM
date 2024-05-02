from fastapi import FastAPI, HTTPException, APIRouter
from app.model.Historial import Historial
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()

class HistorialRequest(BaseModel):
    id: int
    id_usuario: int
    tabla_afectada: str
    accion: str
    fecha_hora: str


@router.get("/Historial/", response_model=List[HistorialRequest])
def ListadoHistorial():

    historial = Historial()
    response = historial.get_all()
    return response


# Agregar el router a la aplicación FastAPI
app = FastAPI()
app.include_router(router)