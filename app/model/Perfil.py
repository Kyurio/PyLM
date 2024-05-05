from http.client import HTTPException
from app.database.Conexion import Conexion
from app.schemas.SchemaPerfil import PerfilCreateModel, PerfilSelectModel
from typing import List

class Perfil:

    tabla = "perfil"

    @staticmethod
    def create(nombre_perfil: str, descripcion: str, estado: bool) -> int:
        with Conexion() as db:
            try:

                query = (f"INSERT INTO {Perfil.tabla} (nombre_perfil, descripcion, estado, created_at, updated_at) VALUES "
                         f"(%s, %s, %s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (nombre_perfil, descripcion, estado,))

                if result:
                    return True
                else:
                    return False

            except Exception as e:
                print(f"Error al crear perfil: {e}")
                raise

    @staticmethod
    def get(id: int) -> PerfilSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Perfil.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                if result:
                    row = result[0]
                    return PerfilSelectModel(
                        id=row[0],
                        id_perfil=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener perfil: {e}")
                raise

    @staticmethod
    def update(quest_id: int, nombre_perfil: str, descripcion: str, estado: bool) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {Perfil.tabla} SET nombre_perfil = %s, descripcion = %s, estado = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (nombre_perfil, descripcion, estado, quest_id))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar perfil: {e}")
                raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Perfil.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar perfil: {e}")
                raise

    @staticmethod
    def get_all() -> List[PerfilSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Perfil.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(PerfilSelectModel(
                        id=row[0],
                        nombre_perfil=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los perfiles: {e}")
            raise
