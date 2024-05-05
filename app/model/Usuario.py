from app.database.Conexion import Conexion
from app.schemas.SchemaUsuario import UsuarioCreateModel, UsuarioSelectModel
from typing import List


class Usuarios:
    tabla = "usuario"

    @staticmethod
    def create(data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {Usuarios.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def get(id: int) -> UsuarioSelectModel:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                row = result[0] if result else None
                return UsuarioSelectModel(*row) if row else None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None

    @staticmethod
    def update(quest_id: int, usuario: str, nombre: str, password: str, correo: str, estado: bool) -> UsuarioSelectModel:
        try:
            with Conexion() as db:
                query = f"UPDATE {Usuarios.tabla} SET usuario = %s, nombre = %s, password = %s, correo = %s, estado = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (usuario, nombre, password, correo, estado, quest_id))
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return UsuarioSelectModel(
                        id=row[0],
                        id_perfil=row[1],
                        usuario=row[2],
                        password=row[3],
                        correo=row[4],
                        estado=row[5],
                    )
                else:
                    return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        try:
            with Conexion() as db:
                query = f"DELETE FROM {Usuarios.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    @staticmethod
    def get_all() -> List[UsuarioSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(UsuarioSelectModel(
                        id=row[0],
                        id_perfil=row[1],
                        usuario=row[2],
                        password=row[3],
                        correo=row[4],
                        estado=row[5],
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
