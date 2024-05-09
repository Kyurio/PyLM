from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controller.Secuencia import PostSecuencia
from app.controller.Concepto import PostConcepto
from app.controller.Movimiento import PostMovimiento
from app.controller.PlanMovimiento import PostPlanMovimiento

router = APIRouter()

@router.post("/PostCargarPlanMinero/")
def cargar_datos_desde_excel(file: UploadFile):
    try:
        # Datos estáticos
        secuencia = {"descripcion": "Descripción de la secuencia estática"}
        concepto = {"nombre": "Nombre del concepto estático"}
        movimiento = {"id_plan_movimiento": 1, "descripcion": "Descripción del movimiento estático"}
        plan_movimiento = {"id_movimiento": 1, "fecha": "2024-05-08T17:25:55.814Z"}

        # Insertar datos estáticos y obtener los resultados
        resultado_secuencia = PostSecuencia.crear_secuencia(secuencia)
        resultado_concepto = PostConcepto.crear_concepto(concepto)
        resultado_movimiento = PostMovimiento.crear_movimiento(movimiento)
        resultado_plan_movimiento = PostPlanMovimiento.crear_plan_movimiento(plan_movimiento)

        # Imprimir los resultados
        print("Resultado secuencia:", resultado_secuencia)
        print("Resultado concepto:", resultado_concepto)
        print("Resultado movimiento:", resultado_movimiento)
        print("Resultado plan movimiento:", resultado_plan_movimiento)

    except Exception as e:
        print(f"Error al cargar datos estáticos: {str(e)}")
