Prueba Técnica: Gestión de Estudiantes y Calificaciones
Contexto:
Eres un desarrollador en una escuela que necesita un programa para manejar las calificaciones de los estudiantes. Se te pide que implementes un sistema básico con las siguientes funcionalidades.

Requisitos:
Almacenar datos de estudiantes y sus calificaciones.

Cada estudiante tiene un nombre y una lista de calificaciones (pueden ser números enteros o decimales).
Ejemplo:
estudiantes = {
    "Juan": [85, 90, 78],
    "Ana": [92, 88, 84],
    "Luis": [70, 75, 80]
}
Funcionalidad 1: Agregar un estudiante.

Escribe una función agregar_estudiante(nombre, calificaciones) que agregue un nuevo estudiante al diccionario.
Funcionalidad 2: Calcular el promedio de un estudiante.

Escribe una función calcular_promedio(nombre) que devuelva el promedio de las calificaciones de un estudiante dado.
Si el estudiante no existe, la función debe manejarlo con un mensaje adecuado.
Funcionalidad 3: Obtener al estudiante con el mejor promedio.

Escribe una función mejor_estudiante() que devuelva el nombre del estudiante con el promedio más alto.
Funcionalidad 4: Eliminar un estudiante.

Escribe una función eliminar_estudiante(nombre) que elimine al estudiante del diccionario.