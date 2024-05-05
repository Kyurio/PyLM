from app.database.Conexion import Conexion
from app.schemas.SchemaUsuario import UsuarioResponseModel
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
    def get(id: int) -> UsuarioResponseModel:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                row = result[0] if result else None
                return UsuarioResponseModel(*row) if row else None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None

    @staticmethod
    def update(quest_id: int, usuario: str, nombre: str, password: str, correo: str, estado: bool) -> bool:
        try:
            with Conexion() as db:
                query = f"UPDATE {Usuarios.tabla} SET usuario = %s, nombre = %s, password = %s, correo = %s, estado = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (usuario, nombre, password, correo, estado, quest_id))
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

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
    def get_all() -> List[UsuarioResponseModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla}"
                result = db.execute(query)
                return [UsuarioResponseModel(*row) for row in result]
        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
