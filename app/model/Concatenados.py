from typing import List
from pydantic import BaseModel
from datetime import datetime
from app.database.Conexion import Conexion

class ResponseConcatenados(BaseModel):
    id: int
    descripcion: str
    created_at: datetime
    updated_at: datetime

from typing import List
from datetime import datetime

class Concatenados:
    tabla = "Concatenados"

    @staticmethod
    def create(descripcion: str) -> int:
        with Conexion() as db:
            try:
                query = (f"INSERT INTO {Concatenados.tabla} (descripcion, created_at, updated_at) VALUES "
                         f"(%s, NOW(), NOW()) RETURNING id")
                result = db.execute(query, (descripcion))
                if result:
                    return result[0][0]  # Devuelve el ID del Concatenados creado
                else:
                    return None
            except Exception as e:
                print(f"Error al crear Concatenados: {e}")
                raise

    @staticmethod
    def get(quest_id: int) -> ResponseConcatenados:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Concatenados.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return ResponseConcatenados(
                        id=row[0],
                        nombre_Concatenados=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return None
            except Exception as e:
                print(f"Error al obtener Concatenados: {e}")
                raise

    @staticmethod
    def update(id: int, descripcion: str) -> bool:
        with Conexion() as db:
            try:
                query = f"UPDATE {Concatenados.tabla} SET descripcion = %s, updated_at = NOW() WHERE id = %s"
                db.execute(query, (descripcion, quest_id))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar Concatenados: {e}")
                raise

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Concatenados.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Concatenados: {e}")
                raise

    @staticmethod
    def get_all() -> List[ResponseConcatenados]:
        try:
            with Conexion() as db:
                query = f"SELECT * FROM {Concatenados.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(ResponseConcatenados(
                        id=row[0],
                        descripcion=row[1],
                        created_at=row[2],
                        updated_at=row[3]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos los Concatenadoses: {e}")
            raise
