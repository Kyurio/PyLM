import os
from dotenv import load_dotenv
import psycopg2


class Conexion:
    def __init__(self, env_path='.env'):
        self.env_path = env_path
        self.load_env()  # Cargar las variables de entorno desde el archivo .env
        self.connection = None

    def load_env(self):
        load_dotenv(self.env_path)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv("DB_SERVER"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                port=os.getenv("DB_PORT"),
            )
            print("Conexión exitosa a la base de datos PostgreSQL")
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos PostgreSQL: {e}")
            raise

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                print("Conexión a la base de datos PostgreSQL cerrada")
            except psycopg2.Error as e:
                print(f"Error al cerrar la conexión: {e}")

    def execute(self, query, values=None):
        print("Consulta ejecutada:", query)
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    if values:
                        cursor.execute(query, values)
                    else:
                        cursor.execute(query)

                    # Para consultas SELECT, devolver los resultados
                    if query.strip().lower().startswith("select"):
                        result = cursor.fetchall()
                        return result
                    # Para consultas INSERT, devolver el ID generado
                    elif query.strip().lower().startswith("insert"):
                        self.connection.commit()
                        return cursor.lastrowid  # Esto puede variar según la base de datos utilizada
                    # Para otras consultas, devolver el número de filas afectadas
                    else:
                        self.connection.commit()
                        return cursor.rowcount
            except psycopg2.Error as e:
                print(f"Error al ejecutar la consulta: {e}")
                return None
        else:
            print("No hay conexión activa a la base de datos PostgreSQL")
            return None
