from fastapi import APIRouter, UploadFile, File
from app.controller.SecuenciaDeCarga import CargaForcast

router = APIRouter()

@router.post("/CreateForcast/")
def crear_forcast(fecha: str, file: UploadFile = File(...)):
    return  CargaForcast(fecha, file)

