from app.database.Conexion import Conexion

class Auth:
    tabla = "usuario"

    @classmethod
    def authenticate(cls, identificador, clave):
        db_connector = Conexion()  # Utiliza la clase de conexión
        try:

            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE (correo= %s OR usuario = %s) AND password = %s AND estado = true"
            result = db_connector.execute(query, [identificador, identificador, clave])
            return result

        finally:
            db_connector.close()  # Cierra la conexión a la base de datos

    @classmethod
    def verify_user_existence(cls, identificador):

        db_connector = Conexion()  # Utiliza la clase de conexión
        try:
            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE correo = %s OR usuario = %s"
            result = db_connector.execute(query, [identificador, identificador])
            return result

        finally:
            db_connector.close()  # Cierra la conexión a la base de datos
