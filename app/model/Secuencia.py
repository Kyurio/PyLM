from app.database.Conexion import Conexion
from app.schemas.SchemaSecuencia import SecuenciaCreateModel, SecuenciaSelectModel
from typing import List


class Secuencia:

    tabla = "secuencia"

    @staticmethod
    def create(descripcion: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Secuencia.tabla} (descripcion, created_at, updated_at) VALUES "
                         f"(%s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (descripcion))
                if result:
                    return True
                else:
                    return False

            except Exception as e:
                raise

    @staticmethod
    def get(quest_id: int) -> SecuenciaSelectModel:
        with Conexion() as db:
            try:

                query = f"SELECT * FROM {Secuencia.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return SecuenciaSelectModel(
                        id=row[0],
                        nombre_Secuencia=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None

            except Exception as e:
                raise

    @staticmethod
    def update(id: int, descripcion: str) -> bool:
        with Conexion() as db:
            try:

                query = f"UPDATE {Secuencia.tabla} SET descripcion = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (descripcion, quest_id))
                db.connection.commit()
                return True

            except Exception as e:

                return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:

                query = f"DELETE FROM {Secuencia.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True

            except Exception as e:
                return False

    @staticmethod
    def get_all() -> List[SecuenciaSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Secuencia.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(SecuenciaSelectModel(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            raise
