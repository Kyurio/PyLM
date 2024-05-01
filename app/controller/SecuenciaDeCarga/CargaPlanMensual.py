import pandas as pd

def leer_excel(ruta_excel):
    try:
        # Lee el archivo Excel
        excel_data = pd.read_excel(ruta_excel, sheet_name='Nombre_de_la_primera_hoja')
        return excel_data
    except Exception as e:
        return None, str(e)

# Ejemplo de uso
ruta_excel = input("Por favor, introduce la ruta al archivo Excel: ")
datos_excel = leer_excel(ruta_excel)

if datos_excel is not None:
    print("Datos leídos correctamente del archivo Excel:")
    print(datos_excel)  # Muestra todos los datos leídos del Excel
else:
    print("Error al leer el archivo Excel.")
