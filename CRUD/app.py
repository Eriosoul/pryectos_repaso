from connection import DataBaseBook
from flask import Flask

app = Flask(__name__)
db = DataBaseBook()  # Conexión activa al iniciar la app

@app.route("/home", methods=['GET'])
def home():
    count = db.get_data_count()  # Llamada a la base de datos desde la ruta
    return f"Hello, world! Total de registros en 'books': {count}"

@app.route("/count", methods=['GET'])
def count():
    total_books = db.get_data_sql()  # Obtén el conteo de registros en la tabla
    return f"Total de libros en 'books': {total_books}"


@app.route("/close", methods=['GET'])
def close():
    db.close_connection()  # Cierra la conexión de la base de datos
    return "Conexión cerrada"

if __name__ == '__main__':
    try:
        app.run(debug=True, port=4000)
    except Exception as e:
        print("Error al iniciar la aplicación:", e)


        