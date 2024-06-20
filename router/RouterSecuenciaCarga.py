from fastapi import APIRouter, UploadFile, File
from app.controller.SecuenciaDeCarga import CargaPlanMensual, GetPlanMensual

router = APIRouter()

@router.post("/CreatePlanMensual/")
def crear_secuencia_route(fecha: str, file: UploadFile = File(...)):
    return CargaPlanMensual(fecha, file)


@router.get("/GetPlanMensual")
def listar_secuencia_carga():
    return GetPlanMensual()