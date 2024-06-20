from app.database.Conexion import Conexion
from app.schemas.SchemaConcepto import ConceptoSelectModel
from typing import List


class Conceptos:
    tabla = "conceptos"

    @staticmethod
    def create(data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Conceptos.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def get(id: int) -> ConceptoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Conceptos.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
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
                    return False

            except Exception as e:
                print(f"Error al obtener Conceptos: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Conceptos.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

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
                        nombre=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows

        except Exception as e:
            print(f"Error al obtener todos los Conceptoses: {e}")
            raise

    @staticmethod
    def get_last_id() -> int:
        with Conexion() as db:
            try:
                query = f"SELECT MAX(id) FROM {Conceptos.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None