Ejercicio 1: Crear una API RESTful Básica con Flask
Objetivo: Crear una API RESTful sencilla que permita gestionar una lista de tareas pendientes (To-Do list). La API deberá ser capaz de:

- Obtener todas las tareas (GET /tasks).
- Añadir una nueva tarea (POST /tasks).
- Actualizar una tarea existente (PUT /tasks/<id>).
- Eliminar una tarea (DELETE /tasks/<id>).
Requisitos:
  Utiliza Flask como framework para construir la API.

  Debe haber un modelo de datos básico para las tareas, que incluya:

   - id: un identificador único.
   - title: el título de la tarea.
   - description: una descripción corta de la tarea.
   - done: un valor booleano que indique si la tarea está completada o no.
   - No es necesario guardar los datos en una base de datos real, puedes almacenarlos en una lista en memoria.

Detalles:
  Inicialmente, la API debería devolver una lista vacía de tareas.
  Deberás usar las rutas HTTP correctas para cada acción (GET, POST, PUT, DELETE).
  Deberías asegurarte de manejar posibles errores (por ejemplo, cuando se intenta actualizar una tarea que no existe).
  Rutas de la API:
    - GET /tasks: Devuelve la lista de todas las tareas.
    - POST /tasks: Crea una nueva tarea. El cuerpo de la petición debe incluir title, description, y done (por defecto puede ser False).
    - PUT /tasks/<id>: Actualiza una tarea existente según su id.
    - DELETE /tasks/<id>: Elimina la tarea con el id dado.
Ejemplo de una tarea:
json
  Copiar código
  {
    "id": 1,
    "title": "Comprar leche",
    "description": "Comprar 2 litros de leche para el desayuno",
    "done": false
  }
Sugerencias:
Usa Flask y si lo deseas, Postman o cURL para probar tu API.
Utiliza el código limpio, organizando las rutas y manejando los posibles errores.
Trata de manejar correctamente las respuestas HTTP con los códigos apropiados (200, 404, etc.).
Pista:
Piensa en cómo organizar las rutas y cómo podrías almacenar y acceder a la lista de tareas dentro de la API sin necesidad de base de datos. También, es útil usar funciones para abstraer lógica repetitiva (como buscar una tarea por ID).
