from fastapi import APIRouter, UploadFile, File
from app.controller.SecuenciaDeCarga import CargaPlanMensual

router = APIRouter()

@router.post("/CreateSecuencia/")
def crear_secuencia_route(file: UploadFile = File(...)):
    return CargaPlanMensual(file)


