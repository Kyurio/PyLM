from app.database.Conexion import Conexion

class Auth:
    tabla = "usuario"

    @classmethod
    def authenticate(cls, email, clave):
        db_connector = Conexion()  # Utiliza la clase de conexión
        try:

            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE correo= %s AND password = %s"
            result = db_connector.execute(query, [email, clave])
            return result

        finally:
            db_connector.close()  # Cierra la conexión a la base de datos

    @classmethod
    def verify_user_existence(cls, email):

        db_connector = Conexion()  # Utiliza la clase de conexión
        try:
            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE correo = %s"
            result = db_connector.execute(query, [email])
            return result

        finally:
            db_connector.close()  # Cierra la conexión a la base de datos
