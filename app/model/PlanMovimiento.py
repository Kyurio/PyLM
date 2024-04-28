from app.database.Conexion import Conexion
from app.schemas.SchemaPlanMovimineto import PlanMovimientoSelectModel, PlanMovimientoCreateModel
from typing import List

class PlanMovimiento:
    tabla = "PlanMovimiento"

    @staticmethod
    def create(descripcion: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {PlanMovimiento.tabla} (descripcion, created_at, updated_at) VALUES "
                         f"(%s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (descripcion))
                if result:
                    return result[0][0]  # Devuelve el ID del PlanMovimiento creado
                else:
                    return None
            except Exception as e:
                print(f"Error al crear PlanMovimiento: {e}")
                raise

    @staticmethod
    def get(quest_id: int) -> PlanMovimientoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {PlanMovimiento.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return PlanMovimientoSelectModel(
                        id=row[0],
                        nombre_PlanMovimiento=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener PlanMovimiento: {e}")
                raise

    @staticmethod
    def update(id: int, descripcion: str) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {PlanMovimiento.tabla} SET descripcion = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (descripcion, id))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar PlanMovimiento: {e}")
                raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {PlanMovimiento.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar PlanMovimiento: {e}")
                raise

    @staticmethod
    def get_all() -> List[PlanMovimientoSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {PlanMovimiento.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(PlanMovimientoSelectModel(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los PlanMovimientoes: {e}")
            raise
