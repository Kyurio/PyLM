from fastapi import APIRouter
from app.controller.InfoRiego import PostInfoRiego, GetInfoRiego, DeleteInfoRiego, UpdateInfoRiego
from app.schemas.SchemaInfoRiego import InfoRiegoCreateModel, InfoRiegoSelectModel
from typing import List

router = APIRouter()


@router.get("/GetInfoRiego", response_model=List[InfoRiegoSelectModel])
def listar_info_riego_route():
    return GetInfoRiego()


@router.post("/CreateInfoRiego/")
def crear_info_riego_route(request: InfoRiegoCreateModel):
    return PostInfoRiego(request)


@router.put("/UpdateInfoRiego/{id}")
def actualizar_info_riego_route(id: int, request: InfoRiegoCreateModel):
    return UpdateInfoRiego(id, request)


@router.delete("/DeleteInfoRiego/{id}")
def eliminar_info_riego_route(id: int):
    return DeleteInfoRiego(id)
