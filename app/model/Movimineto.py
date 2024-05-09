from app.database.Conexion import Conexion
from app.schemas.SchemaMovimiento import MovimientoSelectModel,MovimientoCreateModel
from typing import List

class Movimientos:
    tabla = "Movimientos"


    @staticmethod
    def create(descripcion: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Movimientos.tabla} (id_concepto, id_secuencia, valor) VALUES "
                         f"(%s, %s, %s) RETURNING id")
                result = db.execute(query, (descripcion,))
                if result:
                    return True
                else:
                    return None
            except Exception as e:
                print(f"Error al crear Movimientos: {e}")
                raise

    @staticmethod
    def get(quest_id: int) -> MovimientoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Movimientos.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return MovimientoSelectModel(
                        id=row[0],
                        nombre_Movimientos=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener Movimientos: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Movimientos.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False


    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Movimientos.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Movimientos: {e}")
                raise

    @staticmethod
    def get_all() -> List[MovimientoSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Movimientos.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(MovimientoSelectModel(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Movimientoses: {e}")
            raise
