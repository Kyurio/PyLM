import pandas as pd
import io
from datetime import datetime, timedelta
from fastapi import APIRouter, UploadFile, HTTPException, File
from concurrent.futures import ThreadPoolExecutor, as_completed

from app.controller.Concepto import PostConcepto, GetLastID as idConcepto, GetConcepto as GetAllConceptos
from app.controller.Secuencia import PostSecuencia, GetLastID as idSecuencia, GetSecuencia as GetAllSecuencias
from app.controller.Movimiento import PostMovimiento
from app.schemas.SchemaConcepto import ConceptoCreateModel
from app.schemas.SchemaSecuencia import SecuenciaCreateModel
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()

def dias_del_mes(mes, anio):
    dias = []
    fecha_inicial = datetime(anio, mes, 1)
    while fecha_inicial.month == mes:
        dias.append(fecha_inicial)
        fecha_inicial += timedelta(days=1)
    return dias

def clean_dataframe(df):
    df = df.dropna(axis=1, how='all')
    df = df.loc[:, ~(df.columns.str.contains('Unnamed') & df.isna().all())]
    return df

def extract_column_data(df, column_name):
    data = df[column_name].dropna().unique().tolist()
    return data

def process_secuencia_item(item):
    secuencia_data = SecuenciaCreateModel(descripcion=str(item))
    try:
        PostSecuencia.crear_secuencia(secuencia_data)
        id_secuencia = idSecuencia.LastID()
        if id_secuencia:
            return id_secuencia
    except HTTPException as e:
        print("Error en process_secuencia_item:", e)
    return None

def process_concepto_item(item):
    if item != 'FECHA':
        concepto_data = ConceptoCreateModel(nombre=item)
        try:
            PostConcepto.crear_concepto(concepto_data)
            id_concepto = idConcepto.LastID()
            if id_concepto:
                return item, id_concepto
        except HTTPException as e:
            print("Error en process_concepto_item:", e)
    return item, None

def process_movimiento_item(id_concepto, id_secuencia, value, date):
    movimiento_data = MovimientoCreateModel(id_concepto=id_concepto, id_secuencia=id_secuencia, valor=value, fecha=date)
    try:
        request = PostMovimiento.crear_movimiento(movimiento_data)
        if request:
            return "datos insertados con exito"
    except HTTPException as e:
        print("Error en process_movimiento_item:", e)

@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:
        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE FINAL DIARIO', engine='openpyxl')
        df = clean_dataframe(df)

        mes = 1
        anio = 2024

        secuencia = extract_column_data(df, df.columns[0])
        conceptos = extract_column_data(df, df.columns[1])

        with ThreadPoolExecutor() as executor:
            future_to_item = {executor.submit(process_secuencia_item, item): item for item in secuencia}
            for future in as_completed(future_to_item):
                future.result()

        with ThreadPoolExecutor() as executor:
            future_to_concepto = {executor.submit(process_concepto_item, item): item for item in conceptos}
            for future in as_completed(future_to_concepto):
                future.result()

        conceptos_guardados = GetAllConceptos.listar_conceptos()

        with ThreadPoolExecutor() as executor:
            for concepto in conceptos_guardados:

                for idx, row in df.iterrows():
                    conceptoExcel = row.iloc[1]
                    if conceptoExcel == concepto.nombre:
                        row_data = row[2:33]  # Ajuste para tomar sólo los días del 1 al 31
                        numeric_data = pd.to_numeric(row_data, errors='coerce')

                        for dia, value in zip(dias_del_mes(mes, anio), numeric_data):
                            if pd.notna(value):
                                future = executor.submit(process_movimiento_item, concepto.id, 1, value, dia)
                                print(future)

    except Exception as e:
        print("Excepción:", str(e))
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")
