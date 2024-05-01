<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, APIRouter
from app.model.Historial import Historial
from app.schemas.SchemaHistorial import HistorialSelectModel
from typing import List
router = APIRouter()

@router.get("/Historial/", response_model=List[HistorialSelectModel])
def ListadoHistorial():

    historial = Historial()
    response = historial.get_all()
    return response

# Agregar el router a la aplicación FastAPI
app = FastAPI()
app.include_router(router)
=======
from fastapi import FastAPI, HTTPException, APIRouter
from app.model.Historial import Historial
from pydantic import BaseModel
from datetime import datetime
from typing import List
# Crear el router
router = APIRouter()


# Definir el modelo de datos para la creación de perfiles
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
>>>>>>> ae38f07e6e86efa63ab0513147f06de5f30d3e1e
