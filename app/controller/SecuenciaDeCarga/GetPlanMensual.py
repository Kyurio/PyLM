from fastapi import APIRouter, HTTPException
from app.model.PlanMensual import PlanMensual
from typing import List

router = APIRouter()

@router.get("/GetPlanMensual/")
def listar_plan_mensual():
    try:
        result = PlanMensual.get_all()
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el plan mensual: {str(e)}")


