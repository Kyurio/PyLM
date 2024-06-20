from app.database.Conexion import Conexion
from app.schemas.SchemaHistorial import HistorialCreateModel, HistorialSelectModel
from typing import List

class Historial:
    tabla = "historial"

    @staticmethod
    def create(id_usuario: int, tabla_afectada: str, accion:str, fecha_hora: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Historial.tabla} (id_usuario, table_afectada, accion, fecha_hora) VALUES "
                         f"(%s, %s, %s, NOW()) RETURNING id")
                result = db.execute(query, (id_usuario, tabla_afectada, accion, fecha_hora,))
                if result:
                    return True
                else:
                    return None

            except Exception as e:
                print(f"Error al crear Historial: {e}")
                raise

    @staticmethod
    def get_all() -> List[HistorialSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Historial.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(HistorialSelectModel(
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
