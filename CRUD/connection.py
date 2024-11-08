import mysql.connector
from mysql.connector import Error
from tqdm import tqdm

class DataBaseBook:
    def __init__(self):
        self.conn = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="library"
            )
            if self.conn.is_connected():
                print("Conexión exitosa")
                print("Información del servidor:", self.conn.get_server_info())
                self.check_or_create_table()
        except Error as ex:
            print("Error en la conexión:", ex)

    def check_or_create_table(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SHOW TABLES LIKE 'books'")
            result = cursor.fetchone()
            if result:
                print("La tabla 'books' ya existe")
            else:
                print("La tabla 'books' no existe. Creando tabla...")
                for _ in tqdm(range(50), desc="Creando tabla 'books'", unit="iter"):
                    pass

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada")

    def get_data_count(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) FROM books')
                count = cursor.fetchone()[0]
                print(f'Total de registros en "books": {count}')
                return count
        except Error as ex:
            print("Error al obtener datos:", ex)
            return None

def test_db():
    db = DataBaseBook()
    db.get_data_count()
    db.close_connection()