from http.client import HTTPException
from app.database.Conexion import Conexion
from app.schemas.SchemaPerfil import PerfilCreateModel, PerfilSelectModel
from typing import List

class Perfil:

    tabla = "perfil"

    @staticmethod
    def create(data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Perfil.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

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
                        estado=row[2],
                        created_at=row[3],
                        updated_at=row[4],
                        created=row[5],
                        updated=row[6],
                        deleted=row[7],
                        leer=row[8]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener perfil: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Perfil.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

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
                        estado=row[2],
                        created_at=row[3],
                        updated_at=row[4],
                        created=row[5],
                        updated=row[6],
                        deleted=row[7],
                        leer=row[8]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los perfiles: {e}")
            raise
