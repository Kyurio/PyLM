import pandas as pd
import io
from fastapi import APIRouter, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse

# imports de controllers
from app.controller.Secuencia import PostSecuencia
from app.controller.Concepto import PostConcepto

# imports de schemas
from app.schemas.SchemaSecuencia import SecuenciaCreateModel
from app.schemas.SchemaConcepto import ConceptoCreateModel

router = APIRouter()


def clean_dataframe(df):
    """ Función para limpiar DataFrame inicial (DataFrame A). """
    df = df.dropna(axis=1, how='all')  # Eliminar columnas completamente vacías
    df = df.loc[:, ~(df.columns.str.contains('Unnamed') & df.isna().all())]  # Eliminar 'Unnamed' sin datos útiles
    return df

def extract_conceptos(df):
    """ Función para extraer los conceptos del DataFrame. """
    conceptos = []
    for index, row in df.iterrows():
        concepto = row[0]
        if pd.notna(concepto) and concepto not in conceptos:
            conceptos.append(concepto)
    return conceptos


@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:

        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE LB DIARIO')
        df = clean_dataframe(df)

        # guarda el plan mensual
        plan_mensual = df.iloc[0, 0]
        pit_lomas = df.iloc[1, 0]
        secuencia_descripcion = f"{plan_mensual} {pit_lomas}"
        secuencia_data = SecuenciaCreateModel(descripcion=secuencia_descripcion)
        response = PostSecuencia.crear_secuencia(secuencia_data)

        # Extraer y guardar los conceptos
        conceptos = extract_conceptos(df)
        for concepto in conceptos:
            concepto_data = ConceptoCreateModel(nombre=concepto)
            response = PostConcepto.crear_concepto(concepto_data)
            print(response)




    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")
