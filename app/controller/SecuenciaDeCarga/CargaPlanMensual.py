# extenciones
from fastapi import APIRouter, UploadFile, HTTPException
import pandas as pd

# controllers
from app.controller.Secuencia import PostSecuencia
from app.controller.Concepto import PostConcepto
from app.controller.Movimiento import PostMovimiento
from app.controller.PlanMovimiento import PostPlanMovimiento

# schemas
from app.schemas.SchemaConcepto import ConceptoCreateModel
from app.schemas.SchemaSecuencia import SecuenciaCreateModel
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()


@router.post("/PostCargarPlanMinero/")
def cargar_datos_desde_excel(file: UploadFile):
    try:

        import pandas as pd

        # Suponiendo que deseas leer todas las columnas con el nombre 'Tonnes'
        concepto = 'Heap a Chancado'
        sheet_name = 'DETALLE LB DIARIO'

        # Leer el archivo Excel completo
        df = pd.read_excel(file.file, sheet_name=sheet_name)

        # Encontrar todas las columnas que contienen el concepto 'Tonnes'
        columnas_tonnes = [col for col in df.columns if concepto in col]

        # Crear un nuevo DataFrame con solo las columnas que contienen el concepto 'Tonnes'
        df_tonnes = df[columnas_tonnes]

        # Imprimir el contenido del DataFrame con las columnas 'Tonnes'
        print(df_tonnes)



    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error al cargar datos desde la hoja '{sheet_name}' del archivo Excel: {str(e)}")
