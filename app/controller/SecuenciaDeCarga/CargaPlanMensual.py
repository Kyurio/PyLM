import pandas as pd
import io
from fastapi import APIRouter, UploadFile, HTTPException, File
from concurrent.futures import ThreadPoolExecutor, as_completed

# Importa los controllers y schemas necesarios
from app.controller.Concepto import PostConcepto, GetLastID as idConcepto, GetConcepto as GetAllConceptos
from app.controller.Secuencia import PostSecuencia, GetLastID as idSecuencia, GetSecuencia as GetAllSecuencias
from app.controller.Movimiento import PostMovimiento
from app.schemas.SchemaConcepto import ConceptoCreateModel
from app.schemas.SchemaSecuencia import SecuenciaCreateModel
from app.schemas.SchemaMovimiento import MovimientoCreateModel

router = APIRouter()

def clean_dataframe(df):
    df = df.dropna(axis=1, how='all')
    df = df.loc[:, ~(df.columns.str.contains('Unnamed') & df.isna().all())]
    return df

def extract_column_data(df, column_name):
    data = df[column_name].dropna().unique().tolist()
    return data

def find_row_by_text(df, text):
    for index, row in df.iterrows():
        if row.astype(str).str.contains(text).any():
            return row
    return None

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

# Función para procesar cada item de movimiento
def process_movimiento_item(id_concepto, id_secuencia, value, date):
    print(f"Valor: {value}, Fecha: {date}")
    movimiento_data = MovimientoCreateModel(id_concepto=id_concepto, id_secuencia=id_secuencia, valor=value)
    try:
        # Aquí solo mostramos los datos capturados, no insertamos en la base de datos por ahora
        print(f"Insertando movimiento: id_concepto={id_concepto}, id_secuencia={id_secuencia}, valor={value}, fecha={date}")
        # PostMovimiento.crear_movimiento(movimiento_data)  # Comentado por ahora
    except HTTPException as e:
        print("Error en process_movimiento_item:", e)
    except Exception as e:
        print("Error inesperado en process_movimiento_item:", e)

@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:
        # Leer el archivo completo y mantenerlo en memoria
        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE FINAL DIARIO', engine='openpyxl')
        df = clean_dataframe(df)

        # Obtener las fechas desde las columnas (suponiendo que las fechas están en las columnas 3 a 34)
        dates = pd.to_datetime(df.columns[3:34], errors='coerce').dropna()

        # Obtener los datos en memoria
        secuencia = extract_column_data(df, df.columns[0])
        conceptos = extract_column_data(df, df.columns[1])

        print(f"Secuencia: {secuencia}")
        print(f"Conceptos: {conceptos}")

        # Procesar las secuencias en paralelo
        with ThreadPoolExecutor() as executor:
            future_to_item = {executor.submit(process_secuencia_item, item): item for item in secuencia}
            for future in as_completed(future_to_item):
                future.result()  # No necesitamos almacenar los resultados ahora

        # Procesar los conceptos en paralelo
        with ThreadPoolExecutor() as executor:
            future_to_concepto = {executor.submit(process_concepto_item, item): item for item in conceptos}
            for future in as_completed(future_to_concepto):
                future.result()  # No necesitamos almacenar los resultados ahora

        # Obtener conceptos guardados de la base de datos
        conceptos_guardados = GetAllConceptos.listar_conceptos()
        concepto_ids = {concepto.nombre: concepto.id for concepto in conceptos_guardados}

        # Obtener secuencias guardadas de la base de datos
        secuencias_guardadas = GetAllSecuencias.listar_secuencia()
        secuencia_ids = {secuencia.descripcion: secuencia.id for secuencia in secuencias_guardadas}

        # Procesar movimientos y mostrar valores y fechas
        with ThreadPoolExecutor() as executor:
            future_to_movimiento = {}
            for concepto in conceptos_guardados:
                print("este es el concepto buscado: ", concepto.nombre)
                row_data = df[df.iloc[:, 0] == concepto.nombre]
                print("este es el concepto del excel", row_data)
                if row_data.empty:
                    print(f"No se encontró la fila para el concepto: {concepto}")
                    continue

                row_data = row_data.iloc[0, 1:]  # Ignorar la primera columna que es el nombre del concepto
                numeric_data = pd.to_numeric(row_data, errors='coerce').dropna()

                if len(numeric_data) != len(dates):
                    print(f"Datos numéricos y fechas no coinciden para el concepto: {concepto}")
                    continue

                print(f"Procesando concepto: {concepto} con id_concepto={id_concepto}")
                for i, (value, date) in enumerate(zip(numeric_data, dates)):
                    id_secuencia = secuencia_ids.get(i + 1)
                    if pd.isna(value):
                        continue  # Ignorar valores NaN

                    future = executor.submit(process_movimiento_item, id_concepto, id_secuencia, value, date)
                    future_to_movimiento[future] = (id_concepto, id_secuencia)

            for future in as_completed(future_to_movimiento):
                try:
                    future.result()  # Procesar resultado, aunque no lo necesitamos ahora
                    print(f"Movimiento procesado: {future_to_movimiento[future]}")
                except Exception as e:
                    print(e)

    except Exception as e:
        print("Excepción:", str(e))
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")
