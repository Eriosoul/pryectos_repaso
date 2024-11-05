Ejercicio 2: API con Flask, Validación y Simulación de Persistencia en SQLite
Objetivo: Crear una API de "Gestión de Libros" que permita almacenar, actualizar y eliminar información sobre libros. 
Esta vez vamos a:

    Introducir validación de datos.
    Agregar una base de datos SQLite para simular persistencia de datos.
    Crear consultas avanzadas que filtren y ordenen los datos.
Especificaciones del API
La API debe permitir:
    Listar todos los libros (GET /books): Devuelve todos los libros con opción de filtro por autor y ordenamiento por fecha de publicación.
    Añadir un libro (POST /books): Crea un nuevo libro.
    Actualizar un libro (PUT /books/<id>): Actualiza los detalles de un libro existente.
    Eliminar un libro (DELETE /books/<id>): Elimina un libro de la base de datos.
    Cada libro debe incluir la siguiente información:

    id (generado automáticamente por la base de datos).
    title (obligatorio).
    author (obligatorio).
    published_date (obligatorio, en formato YYYY-MM-DD).
    genre (opcional).
    price (opcional, debe ser un número positivo).

Requisitos:
    Base de Datos SQLite: Crea una base de datos library.db y una tabla books para almacenar los datos de los libros.
    Validación de Datos: Asegúrate de que title, author, published_date sean obligatorios y que price sea un número positivo. Usa marshmallow o Flask-Inputs para manejar la validación.
    Manejo de Errores: Devuelve un error 400 Bad Request con mensajes claros cuando los datos son inválidos y un 404 Not Found si se intenta acceder a un libro inexistente.
    Ejemplo de un libro
    json
    Copiar código
        {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": "1960-07-11",
        "genre": "Fiction",
        "price": 18.99
        }
        
Rutas de la API
    GET /books: Devuelve una lista de todos los libros, con filtros opcionales.
    POST /books: Crea un nuevo libro.
    PUT /books/<id>: Actualiza un libro existente por su id.
    DELETE /books/<id>: Elimina un libro de la base de datos.
    Recomendaciones Adicionales
    ORM Opcional: Para manejar la base de datos SQLite, podrías usar SQLAlchemy para facilitar las consultas.
    Pruebas con Postman o cURL: Prueba la API y asegúrate de que la validación y los códigos de estado sean correctos.
    Ordenamiento por Fecha: Permite que los usuarios de la API ordenen la lista de libros por fecha de publicación (?sort_by=date).
