from typing import List
from pydantic import BaseModel
from datetime import datetime
from app.database.Conexion import Conexion

class ResponseHistorial(BaseModel):
    id: int
    id_usuario: int
    tabla_afectada: str
    accion: str
    fecha_hora: str

from typing import List
from datetime import datetime

class Historial:
    tabla = "historial"

    @staticmethod
    def create(id_usuario: int, tabla_afectada: str, accion:str, fecha_hora: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Historial.tabla} (id_usuario, table_afectada, accion, fecha_hora) VALUES "
                         f"(%s, %s, %s, NOW()) RETURNING id")
                result = db.execute(query, (nombre_Historial, descripcion, estado))
                if result:
                    return result[0][0]  # Devuelve el ID del Historial creado
                else:
                    return None
            except Exception as e:
                print(f"Error al crear Historial: {e}")
                raise

    @staticmethod
    def get_all() -> List[ResponseHistorial]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Historial.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(ResponseHistorial(
                        id=row[0],
                        id_usuario=row[1],
                        tabla_afectada=row[2],
                        accion=row[3],
                        fecha_hora=row[4]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Historiales: {e}")
            raise
