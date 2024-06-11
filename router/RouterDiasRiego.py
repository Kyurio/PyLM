from fastapi import APIRouter
from app.controller.DiasRiego import PostDiasRiego, GetDiasRiego, DeleteDiasRiego, UpdateDiasRiego
from app.schemas.SchemaDiasRiego import DiasRiegoCreateModel, DiasRiegoSelectModel
from typing import List

router = APIRouter()


@router.get("/GetDiasRiego", response_model=List[DiasRiegoSelectModel])
def listar_dias_riego_route():
    return GetDiasRiego()


@router.post("/CreateDiasRiego/")
def crear_dias_riego_route(request: DiasRiegoCreateModel):
    return PostDiasRiego(request)


@router.put("/UpdateDiasRiego/{id}")
def actualizar_dias_riego_route(id: int, request: DiasRiegoCreateModel):
    return UpdateDiasRiego(id, request)


@router.delete("/DeleteDiasRiego/{id}")
def eliminar_dias_riego_route(id: int):
    return DeleteDiasRiego(id)
