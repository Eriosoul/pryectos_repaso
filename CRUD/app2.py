from flask import Flask
from connection import DataBaseBook

app = Flask(__name__)

def test_db():
    try:
        db = DataBaseBook()
        db.get_conncetion()
        return db  # Retorna la instancia de conexión si es exitosa
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

db = test_db()
if db:  # Solo inicia la app si hay conexión
    @app.route("/home", methods=['GET'])
    def home():
        return "Hello world"

    @app.route("/count", methods=['GET'])
    def count():
        total_books = db.get_data_sql()
        return f"Total de libros en 'books': {total_books}"

    if __name__ == '__main__':
        try:
            app.run(debug=True, port=4000)
        finally:
            db.close_connection()
else:
    print("No se pudo establecer la conexión con la base de datos. La aplicación no se iniciará.")
