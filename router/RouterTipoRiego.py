from fastapi import APIRouter
from app.controller.TipoRiego import PostTipoRiego, GetTipoRiego, DeleteTipoRiego, UpdateTipoRiego
from app.schemas.SchemaTipoRiego import TipoRiegoCreateModel, TipoRiegoSelectModel
from typing import List

router = APIRouter()


@router.get("/GetTipoRiego", response_model=List[TipoRiegoSelectModel])
def listar_tipo_riego_route():
    return GetTipoRiego()


@router.post("/CreateTipoRiego/")
def crear_tipo_riego_route(request: TipoRiegoCreateModel):
    return PostTipoRiego(request)


@router.put("/UpdateTipoRiego/{id}")
def actualizar_tipo_riego_route(id: int, request: TipoRiegoCreateModel):
    return UpdateTipoRiego(id, request)


@router.delete("/DeleteTipoRiego/{id}")
def eliminar_tipo_riego_route(id: int):
    return DeleteTipoRiego(id)
