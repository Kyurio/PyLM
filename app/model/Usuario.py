from app.database.Conexion import Conexion
<<<<<<< HEAD
from app.schemas.SchemaUsuario import UsuarioResponseModel
from typing import List

=======
from app.schemas.SchemaUsuario import UsuarioCreateModel, UsuarioSelectModel
from typing import List


>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449
class Usuarios:
    tabla = "usuario"

    @staticmethod
<<<<<<< HEAD
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
=======
    def create(id_perfil: int, usuario: str, password: str, correo: str, estado: bool) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Usuarios.tabla} (id_perfil, usuario, password, correo, estado) VALUES "
                         f"(%s, %s, %s, %s, %s) RETURNING id")
                result = db.execute(query, (id_perfil, usuario, password, correo, estado))
                if result:
                    return True
                else:
                    return False

            except Exception as e:
                print(f"Error al crear usuario: {e}")
                raise
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449

    @staticmethod
    def get(id: int) -> UsuarioResponseModel:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla} WHERE id = %s"
<<<<<<< HEAD
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
=======
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
    def update(quest_id: int, id_perfil, usuario: str, password: str, correo: str, estado: bool) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {Usuarios.tabla} SET id_perfil = %s, usuario = %s, password = %s, correo = %s, estado = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (id_perfil, usuario, password, correo, estado, quest_id))
                db.connection.commit()
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449
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
<<<<<<< HEAD
                return [UsuarioResponseModel(*row) for row in result]
=======
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
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449
        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
