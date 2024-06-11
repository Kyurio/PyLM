from app.database.Conexion import Conexion
from app.schemas.SchemaDiasRiego import DiasRiegoSelectModel
from typing import List

class DiasRiego:
    tabla = "dias_riego"

    @staticmethod
    def create(data: dict) -> bool:

        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {DiasRiego.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)

                return True
        except Exception as e:
            return False

    @staticmethod
    def get(quest_id: int) -> DiasRiegoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {DiasRiego.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return DiasRiegoSelectModel(
                        id=row[0],
                        nombre_DiasRiego=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener DiasRiego: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {DiasRiego.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar dia de riego: {e}")
            return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {DiasRiego.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar dia de riego: {e}")
                raise

    @staticmethod
    def get_all() -> List[DiasRiegoSelectModel]:
        try:

            with Conexion() as db:
                query = f"SELECT * FROM {DiasRiego.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(DiasRiegoSelectModel(
                        id=row[0],
                        id_tipo_riego=row[1],
                        id_concatenado=row[2],
                        id_loma=row[3],
                        fecha=row[4],
                        horas_de_riego=row[5],
                        created_at=row[6],
                        updated_at=row[7]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los dias de riego: {e}")
            raise

    @staticmethod
    def get_last_id() -> int:
        with Conexion() as db:
            try:
                query = f"SELECT MAX(id) FROM {DiasRiego.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None