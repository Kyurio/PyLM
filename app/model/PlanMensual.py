from app.database.Conexion import Conexion
from app.schemas.SchemanSecuenciaCarga import SecuenciaDeCargaSelectModel

class PlanMensual:

    @staticmethod
    def get_all():
        with Conexion() as db:
            try:
                query = "SELECT c.descripcion AS secuencia, b.nombre AS concepto, a.valor, a.fecha FROM movimientos a INNER JOIN conceptos b ON a.id_concepto = b.id INNER JOIN secuencia c ON a.id_secuencia=c.id"
                result = db.execute(query)

                rows = []
                for row in result:
                    rows.append(SecuenciaDeCargaSelectModel(

                        secuencia=row[0],
                        concepto=row[1],
                        valor=row[2],
                        fecha=row[3]
                    ))
                return rows

            except Exception as e:
                print(f"Error al obtener perfil: {e}")
                raise

