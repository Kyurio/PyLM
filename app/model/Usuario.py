from app.database.Conexion import Conexion
from app.schemas.SchemaUsuario import UsuarioCreateModel, UsuarioSelectModel
from typing import List


class Usuarios:
    tabla = "usuario"

    @staticmethod
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

    @staticmethod
    def get(quest_id: int) -> UsuarioSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Usuarios.tabla} WHERE id = %s"
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
                return True
            except Exception as e:
                print(f"Error al actualizar usuario: {e}")
                raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Usuarios.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar usuario: {e}")
                raise

    @staticmethod
    def get_all() -> List[UsuarioSelectModel]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Usuarios.tabla}"
                print("esta es la consulta: ", query)
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
            raise
