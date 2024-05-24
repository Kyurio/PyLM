from app.database.Conexion import Conexion
from app.schemas.SchemaSecuencia import SecuenciaCreateModel, SecuenciaSelectModel
from typing import List

class Secuencia:
    tabla = "secuencia"

    @staticmethod
    def create(data: dict) -> int:
        with Conexion() as db:
            try:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Secuencia.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                last_id = db.execute(query, values)
                return last_id  # Devolver el ID generado
            except Exception as e:
                print(f"Error al crear usuario: {e}")
                return False

    @staticmethod
    def get(id: int) -> SecuenciaSelectModel:
        with Conexion() as db:
            try:

                query = f"SELECT * FROM {Secuencia.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
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
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Secuencia.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
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

    @staticmethod
    def get_last_id() -> int:
        with Conexion() as db:
            try:
                query = f"SELECT MAX(id) FROM {Secuencia.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None