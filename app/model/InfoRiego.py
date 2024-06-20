from app.database.Conexion import Conexion
from app.schemas.SchemaInfoRiego import InfoRiegoSelectModel
from typing import List

class InfoRiego:
    tabla = "info_riego"

    @staticmethod
    def create(data: dict) -> bool:

        try:
            with Conexion() as db:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                values = list(data.values())
                query = f"INSERT INTO {InfoRiego.tabla} ({columns}, created_at, updated_at) VALUES ({placeholders}, NOW(), NOW())"
                db.execute(query, values)

                return True
        except Exception as e:
            return False

    @staticmethod
    def get(quest_id: int) -> InfoRiegoSelectModel:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {InfoRiego.tabla} WHERE id = %s"
                result = db.execute(query, (quest_id,))
                if result:
                    row = result[0]
                    return InfoRiegoSelectModel(
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
                print(f"Error al obtener 0InfoRiego: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {InfoRiego.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar info de riego: {e}")
            return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {InfoRiego.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar info de riego: {e}")
                raise

    @staticmethod
    def get_all() -> List[InfoRiegoSelectModel]:
        try:

            with Conexion() as db:
                query = f"SELECT * FROM {InfoRiego.tabla}"
                result = db.execute(query)
                rows = []
                for row in result:
                    rows.append(InfoRiegoSelectModel(
                        id=row[0],
                        id_concatenado=row[1],
                        id_loma=row[2],
                        fecha_inicio=row[3],
                        fecha_termino=row[4],
                        largo=row[5],
                        ancho=row[6],
                        status=row[7],
                        volumen=row[8],
                        altura=row[9],
                        area=row[10],
                        tonelaje=row[11],
                        created_at=row[12],
                        updated_at=row[13]
                    ))
                return rows
        except Exception as e:
            print(f"Error al obtener todos las info de riego: {e}")
            raise

    @staticmethod
    def get_last_id() -> int:
        with Conexion() as db:
            try:
                query = f"SELECT MAX(id) FROM {InfoRiego.tabla}"
                result = db.execute(query)
                last_id = result[0][0] if result else None
                return last_id
            except Exception as e:
                print(f"Error al obtener el último ID: {e}")
                return None