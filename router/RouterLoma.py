from fastapi import APIRouter
from app.controller.Loma import PostLoma, GetLoma, DeleteLoma, UpdateLoma
from app.schemas.SchemaLoma import LomaCreateModel, LomaSelectModel
from typing import List

router = APIRouter()


@router.get("/GetLoma", response_model=List[LomaSelectModel])
def listar_loma_route():
    return GetLoma()


@router.post("/CreateLoma/")
def crear_loma_route(request: LomaCreateModel):
    return PostLoma(request)


@router.put("/UpdateLoma/{id}")
def actualizar_loma_route(id: int, request: LomaCreateModel):
    return UpdateLoma(id, request)


@router.delete("/DeleteLoma/{id}")
def eliminar_loma_route(id: int):
    return DeleteLoma(id)
