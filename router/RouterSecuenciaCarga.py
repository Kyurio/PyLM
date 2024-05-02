from fastapi import APIRouter
from app.controller.SecuenciaDeCarga import CargaPlanMensual
from app.schemas.SchemaUsuario import UsuarioSelectModel, UsuarioCreateModel
from typing import List

router = APIRouter()

@router.get("/DetalleLBDiario/", response_model=List[UsuarioSelectModel])
def listar_usuario_route():
    return GetUsuarios()
