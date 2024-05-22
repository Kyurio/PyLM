from app.database.Conexion import Conexion
from app.schemas.SchemaConcatenado import ConcatenadoCreateModel, ConcatenadoSelectModel
from typing import List


class Concatenados:
    tabla = "concatenados"

    @staticmethod
    def create(data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Concatenados.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def get(id: int) -> ConcatenadoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Concatenados.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                if result:
                    row = result[0]
                    return ConcatenadoSelectModel(
                        id=row[0],
                        nombre_Concatenados=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener Concatenados: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Concatenados.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Concatenados.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Concatenados: {e}")
                raise

    @staticmethod
    def get_all() -> List[ConcatenadoSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Concatenados.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(ConcatenadoSelectModel(
                        id=row[0],
                        id_plan_movimiento=[1],
                        descripcion=row[2],
                        created_at=row[3],
                        updated_at=row[4]


                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Concatenadoses: {e}")
            raise

    @staticmethod
    def get_last_id() -> int:
        with Conexion() as db:
            try:
                query = f"SELECT MAX(id) FROM {Concatenados.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None