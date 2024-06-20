from app.database.Conexion import Conexion
from app.schemas.SchemaLoma import LomaCreateModel, LomaSelectModel
from typing import List

class Loma:
    tabla = "lomas"

    @staticmethod
    def create(data: dict) -> int:
        with Conexion() as db:
            try:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Loma.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                last_id = db.execute(query, values)
                return last_id  # Devolver el ID generado
            except Exception as e:
                print(f"Error al crear loma: {e}")
                return False

    @staticmethod
    def get(id: int) -> LomaSelectModel:
        with Conexion() as db:
            try:

                query = f"SELECT * FROM {Loma.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                if result:
                    row = result[0]
                    return LomaSelectModel(
                        id=row[0],
                        nombre=row[1],
                        created_at=row[2],
                        updated_at=row[3]
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
                query = f"UPDATE {Loma.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar loma: {e}")
            return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:

                query = f"DELETE FROM {Loma.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True

            except Exception as e:
                return False

    @staticmethod
    def get_all() -> List[LomaSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Loma.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(LomaSelectModel(
                        id=row[0],
                        nombre=row[1],
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
                query = f"SELECT MAX(id) FROM {Loma.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None