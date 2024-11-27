from flask import Flask, render_template, request, jsonify
from connection import DataBaseBook

app = Flask(__name__)

def test_db():
    try:
        db = DataBaseBook()
        if db.conn and db.conn.is_connected():
            return db
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    return None

# Solo inicia la app si hay conexión
db = test_db()

if db: 
    @app.route("/", methods=['GET'])
    def home():
        return render_template('index.html')
    
    @app.route("/count", methods=['GET'])
    def count():
        total_books = db.get_data_sql()
        return f"Total de libros en 'books': {total_books}"

    @app.route("/get_books", methods=['GET'])
    def get_books():
        books = db.get_all_books()
        return render_template('tabla_libros.html', products=books)
    
    # Ruta para mostrar el formulario
    @app.route("/form_add_books", methods=['GET'])
    def form_add_books():
        return render_template('nuevo_libro.html')
    
    # Ruta para procesar el formulario
    @app.route("/add_books", methods=['POST'])
    def add_books():
        try:
            # Simula datos enviados desde un formulario
            title = request.form['title']
            author = request.form['author']
            published_date = request.form['published_date']
            genre = request.form['genre']
            price = float(request.form['price'])

            # Inserta el libro en la base de datos
            query = """
                INSERT INTO books (title, author, published_date, genre, price)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (title, author, published_date, genre, price))
            db.conn.commit()
            cursor.close()
            return jsonify({'message': 'Libro añadido correctamente'}), 201
        except Exception as e:
            return jsonify({'error': f'Error al añadir el libro: {e}'}), 500
        
    """======================= Metodo Edite / Update ================================"""
    @app.route("/edit_book/<int:book_id>", methods=['GET'])
    def edit_book(book_id):
        try:
            cursor = db.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
            book = cursor.fetchone()  # Obtener los datos del libro
            cursor.close()
            if not book:
                return "Libro no encontrado", 404
            return render_template("edit_book.html", book=book)
        except Exception as e:
            return f"Error al obtener el libro: {e}", 500
    
    @app.route("/update_book/<int:book_id>", methods=['POST'])
    def update_book(book_id):
        try:
            title = request.form['title']
            author = request.form['author']
            published_date = request.form['published_date']
            genre = request.form['genre']
            price = float(request.form['price'])

            query = """
                UPDATE books
                SET title = %s, author = %s, published_date = %s, genre = %s, price = %s
                WHERE id = %s
            """
            cursor = db.conn.cursor()
            cursor.execute(query, (title, author, published_date, genre, price, book_id))
            db.conn.commit()
            cursor.close()
            return "Libro actualizado correctamente", 200
        except Exception as e:
            return f"Error al actualizar el libro: {e}", 500
        
    """ =========== Metodo Delete ========================"""    
    @app.route("/form_delete_books/<int:book_id>", methods=['GET'])
    def form_delete_book(book_id):
        try:
            cursor = db.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
            book = cursor.fetchone()
            cursor.close()
            if not book:
                return "Libro no encontrado", 404
            return render_template("delete_books.html", book=book)
        except Exception as e:
            return f"Error al obtener el libro: {e}", 500
        
    @app.route("/delete_book/<int:book_id>", methods=['POST'])
    def delete_book(book_id):
        try:
            query = "DELETE FROM books WHERE id = %s"
            cursor = db.conn.cursor()
            cursor.execute(query, (book_id,))
            db.conn.commit()
            cursor.close()
            return "Libro eliminado correctamente", 200
        except Exception as e:
            return f"Error al eliminar el libro: {e}", 500
    
    @app.route('/chat')
    def chat():
        return render_template('chat_bot.html', title="Chat Bot")

if __name__ == '__main__':
    try:
        app.run(debug=True, port=4000)
    finally:
        db.close_connection()
else:
    print("No se pudo establecer la conexión con la base de datos. La aplicación no se iniciará.")
