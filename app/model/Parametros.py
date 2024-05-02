from app.database.Conexion import Conexion
from app.schemas.SchemaParametro import ParametroCreateModel, ParametroSelectModel
from typing import List

class Parametros:
    tabla = "Parametros"

    @staticmethod
    def create(descripcion: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Parametros.tabla} (descripcion, created_at, updated_at) VALUES "
                         f"(%s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (descripcion))
                if result:
                    return True
                else:
                    return None
            except Exception as e:
                print(f"Error al crear Parametros: {e}")
                raise

    @staticmethod
    def get(quest_id: int) -> ParametroSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Parametros.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return ParametroSelectModel(
                        id=row[0],
                        nombre_Parametros=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener Parametros: {e}")
                raise

    @staticmethod
    def update(id: int, descripcion: str) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {Parametros.tabla} SET descripcion = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (descripcion, id))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar Parametros: {e}")
                raise

    @staticmethod
    def delete(id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Parametros.tabla} WHERE id = %s"
                db.execute(query, (id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Parametros: {e}")
                raise

    @staticmethod
    def get_all() -> List[ParametroSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Parametros.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(ParametroSelectModel(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Parametroses: {e}")
            raise
