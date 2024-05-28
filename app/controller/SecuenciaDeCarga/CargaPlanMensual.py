import pandas as pd
import io
from fastapi import APIRouter, UploadFile, HTTPException, File
from datetime import datetime, timedelta

# importa los controllers
from app.controller.Concepto import PostConcepto, GetConcepto
from app.controller.Concepto import GetLastID as idConcepto
from app.controller.PlanMovimiento import PostPlanMovimiento

from app.controller.Secuencia import PostSecuencia
from app.controller.Secuencia import GetLastID as idSecuencia
from app.controller.Movimiento import PostMovimiento, GetLastID as idMovimiento
from app.controller.PlanMovimiento.PostPlanMovimiento import crear_plan_movimiento

# importa los schemas
from app.schemas.SchemaConcepto import ConceptoCreateModel, LastID
from app.schemas.SchemaSecuencia import SecuenciaCreateModel, LastID
from app.schemas.SchemaMovimiento import MovimientoCreateModel, LastID
from app.schemas.SchemaPlanMovimineto import PlanMovimientoCreateModel, LastID

router = APIRouter()

def clean_dataframe(df):
    """ Función para limpiar DataFrame inicial (DataFrame A). """
    df = df.dropna(axis=1, how='all')  # Eliminar columnas completamente vacías
    df = df.loc[:, ~(df.columns.str.contains('Unnamed') & df.isna().all())]  # Eliminar 'Unnamed' sin datos útiles
    return df

def extract_column_data(df, column_name):
    """ Función para extraer datos únicos de una columna específica del DataFrame. """
    return df[column_name].dropna().unique().tolist()

def find_row_by_text(df, text):
    """ Función para encontrar la fila que contiene un texto específico. """
    for index, row in df.iterrows():
        if row.astype(str).str.contains(text).any():
            return row
    return None

def identify_date_columns(df):
    # Identificar las columnas que contienen fechas
    date_columns = []
    for col in df.columns:
        if pd.to_datetime(df[col], errors='coerce').notna().sum() > 0:
            date_columns.append(col)
    return date_columns

def get_current_month_days():
    """ Función para capturar el mes actual y generar los 30 días. """
    today = datetime.today()
    start_date = datetime(today.year, today.month, 1)
    days = [start_date + timedelta(days=i) for i in range(30)]
    return days

def listar_conceptos():
    try:
        concepto = GetConcepto.listar_conceptos()
        return concepto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los Conceptos: {str(e)}")

def extraer_nombres_conceptos(conceptos):
    """Función para extraer los nombres de una lista de ConceptoSelectModel."""
    return [concepto.nombre for concepto in conceptos]

@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:
        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE FINAL DIARIO', engine='openpyxl')
        df = clean_dataframe(df)

        # Insertar secuencias
        column_data = extract_column_data(df, df.columns[0])
        for item in column_data:
            secuencia_data = SecuenciaCreateModel(descripcion=str(item))
            response = PostSecuencia.crear_secuencia(secuencia_data)
            if not response:
                raise HTTPException(status_code=500, detail="Error al insertar la secuencia")

        # Insertar conceptos
        conceptos = extract_column_data(df, df.columns[1])
        for item in conceptos:
            if item != 'FECHA':
                concepto_data = ConceptoCreateModel(nombre=item)
                response = PostConcepto.crear_concepto(concepto_data)
                if not response:
                    raise HTTPException(status_code=500, detail="Error al insertar el concepto")

        # Obtener IDs de conceptos y secuencias
        id_concepto = idConcepto.LastID()
        id_secuencia = idSecuencia.LastID()

        if not id_concepto or not id_secuencia:
            raise HTTPException(status_code=500, detail="No se pudieron obtener los IDs de concepto o secuencia")

        # Obtener nombres de conceptos desde la base de datos
        conceptos = listar_conceptos()
        nombres_conceptos = extraer_nombres_conceptos(conceptos)

        for nombre in nombres_conceptos:
            row_data = find_row_by_text(df, nombre)
            if row_data is None:
                continue

            # Convertir datos numéricos
            numeric_data = pd.to_numeric(row_data, errors='coerce').dropna()
            for item in numeric_data:
                movimiento_data = MovimientoCreateModel(id_concepto=id_concepto, id_secuencia=id_secuencia, valor=item)
                response = PostMovimiento.crear_movimiento(movimiento_data)
                if not response:
                    raise HTTPException(status_code=500, detail="Error al insertar el movimiento")

                # Insertar plan movimiento después de cada inserción de movimiento
                id_movimiento = idMovimiento.LastID()
                if not id_movimiento:
                    raise HTTPException(status_code=500, detail="Error al obtener el ID del último movimiento")

                dias_del_mes = get_current_month_days()
                for dia in dias_del_mes:
                    plan_movimiento_data = PlanMovimientoCreateModel(id_movimiento=id_movimiento, fecha=dia.strftime('%Y-%m-%d'))
                    response = PostPlanMovimiento.crear_plan_movimiento(plan_movimiento_data)
                    if not response:
                        raise HTTPException(status_code=500, detail="Error al insertar el plan movimiento")

    except Exception as e:
        print("Excepción:", str(e))
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")
