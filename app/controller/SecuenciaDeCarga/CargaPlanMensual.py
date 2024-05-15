from fastapi import APIRouter, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
import pandas as pd
import io

router = APIRouter()


def get_filtered_data(df, keyword):
    """ Función para filtrar datos basados en una palabra clave """
    row_filter = df.apply(lambda row: keyword in row.to_string(), axis=1)
    selected_row = df[row_filter]
    if not selected_row.empty:
        return selected_row.to_dict(orient='records')
    return {'message': f'No data found for {keyword}'}


@router.post("/PostCargarPlanMinero/")
async def cargar_datos_desde_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="El archivo no es un archivo .xlsx válido.")

    try:
        contents = await file.read()
        data = io.BytesIO(contents)
        df = pd.read_excel(data, sheet_name='DETALLE LB DIARIO')

        # Convertimos todos los datos a string y eliminamos espacios adicionales
        df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)

        # conceptos a insertar
        tonnes_data = get_filtered_data(df, 'Heap Mina a Chancado')
        cut_data = get_filtered_data(df, '%CuT')


        response_data = {
            "Tonnes": tonnes_data,
            "CuT": cut_data
            # Agrega más aquí si es necesario
        }

        print(response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo Excel: {str(e)}")

