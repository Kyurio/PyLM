from fastapi import APIRouter, HTTPException
from app.model.PlanMensual import PlanMensual
from app.schemas.SchemanSecuenciaCarga import SecuenciaDeCargaSelectModel
from typing import List

router = APIRouter()
@router.get("/GetPlanMensual/", response_model=List[SecuenciaDeCargaSelectModel])
def listar_plan_mensual():
    try:

        request = PlanMensual.get_all()
        print("request del controller: ", request)
        return request

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

