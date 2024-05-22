import pandas as pd
import io
from fastapi import APIRouter, UploadFile, HTTPException, File

#importa los controllers
from app.controller.Concepto import PostConcepto
from app.controller.Concepto import  GetLastID as idConcepto

from app.controller.Secuencia import PostSecuencia
from app.controller.Secuencia import GetLastID as idSecuencia

from app.controller.Movimiento import PostMovimiento, GetLastID

#importa los schemas
from app.schemas.SchemaConcepto import ConceptoCreateModel, LastID
from app.schemas.SchemaSecuencia import SecuenciaCreateModel, LastID
from app.schemas.SchemaMovimiento import MovimientoCreateModel, LastID



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


@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:


        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE LB DIARIO', engine='openpyxl')  # Especificar el nombre de la hoja
        df = clean_dataframe(df)

        #########################################################################
        #
        # inserta el concepto
        #
        #########################################################################

        # Identificar el nombre de la columna D
        #column_name = df.columns[1]  # Índice 3 corresponde a la columna D
        #column_data = extract_column_data(df, column_name)
        #for item in column_data:
         #   print(item)
            #concepto_data = ConceptoCreateModel(nombre=item)
            #response = PostConcepto.crear_concepto(concepto_data)

        #########################################################################
        #
        # inserta la secuencia
        #
        #########################################################################
        #column_name = df.columns[0]
        #column_data = extract_column_data(df, column_name)
        #for item in column_data:
            #secuencia_data = SecuenciaCreateModel(descripcion=str(item))
            #response = PostSecuencia.crear_secuencia(secuencia_data)

        #########################################################################
        #
        # inserta la movimiento
        #
        #########################################################################
        id_concepto = idConcepto.LastID()
        id_secuencia = idSecuencia.LastID()

        row_data = find_row_by_text(df, 'Tonnes')
        if row_data is None:
            raise HTTPException(status_code=404, detail="No se encontró una fila que contenga 'Tonnes'.")

        # Filtrar solo los valores numéricos
        numeric_data = pd.to_numeric(row_data, errors='coerce').dropna()

        for item in numeric_data:
            movimiento_data = MovimientoCreateModel(id_concepto=id_concepto, id_secuencia=id_secuencia, valor=item)
            response = PostMovimiento.crear_movimiento(movimiento_data)


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")
