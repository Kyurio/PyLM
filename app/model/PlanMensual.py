from app.database.Conexion import Conexion

class PlanMensual:

    @staticmethod
    def get_all():
        with Conexion() as db:
            try:
                query = f"SELECT sec.* , con.* , mov.* , pmov.*  FROM     secuencia sec INNER JOIN     movimientos mov ON sec.id = mov.id_secuencia INNER JOIN     conceptos con ON con.id = mov.id_concepto INNER JOIN plan_movimiento pmov ON mov.id = pmov.id_movimiento;"
                result = db.execute(query, (id,))

                print("resupuesta: ", result)

            except Exception as e:
                print(f"Error al obtener perfil: {e}")
                raise

