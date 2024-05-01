from app.database.Conexion import Conexion
from app.schemas.SchemaConcepto import ConceptoSelectModel
from typing import List

class Conceptos:
    tabla = "conceptos"

    @staticmethod
    def create(nombre: str) -> int:

        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Conceptos.tabla} (nombre, created_at, updated_at) VALUES "
                         f"(%s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (nombre))
                if result:
                    return result[0][0]
                else:
                    return None
            except Exception as e:
                print(f"Error al crear Conceptos: {e}")
                raise

    @staticmethod
    def get(quest_id: int) -> ConceptoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Conceptos.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return ConceptoSelectModel(
                        id=row[0],
                        nombre_Conceptos=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener Conceptos: {e}")
                raise

    @staticmethod
    def update(id: int, descripcion: str) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {Conceptos.tabla} SET descripcion = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (descripcion, id))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar Conceptos: {e}")
                raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Conceptos.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Conceptos: {e}")
                raise

    @staticmethod
    def get_all() -> List[ConceptoSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Conceptos.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(ConceptoSelectModel(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Conceptoses: {e}")
            raise
