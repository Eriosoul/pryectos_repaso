Prueba Técnica - Python (Junior)
Parte 1: Lógica y Manipulación de Datos
Problema: Escribe una función llamada contar_palabras que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas del texto 
(ignorando mayúsculas y minúsculas) y los valores sean la cantidad de veces que aparece cada palabra.

Entrada:
Una cadena de texto, por ejemplo:
"Hola mundo, hola universo."
Salida esperada:
Un diccionario como:
{'hola': 2, 'mundo': 1, 'universo': 1}
Restricciones:

Ignora la puntuación (coma, punto, etc.).
Considera que las palabras no son sensibles a mayúsculas.
Parte 2: Algoritmo
Problema: Escribe una función llamada numeros_faltantes que reciba una lista de números enteros ordenados en orden ascendente y un rango (inicio y fin). 
La función debe devolver una lista con los números que faltan dentro del rango que no están presentes en la lista.

Entrada:
Una lista y dos enteros representando el rango, por ejemplo:
[1, 2, 4, 6], inicio 1, fin 6.
Salida esperada:
[3, 5].

Parte 3: Pensamiento Crítico
Problema: Se necesita una función llamada analizar_transacciones que reciba una lista de diccionarios, 
donde cada diccionario representa una transacción con las siguientes claves:

id (entero): Identificador único de la transacción.
monto (flotante): Monto de la transacción.
tipo (cadena): Puede ser "ingreso" o "gasto".
La función debe devolver un diccionario con:

El total de ingresos (total_ingresos).

El total de gastos (total_gastos).

La transacción con el mayor gasto.

Entrada:

transacciones = [
    {"id": 1, "monto": 200.0, "tipo": "ingreso"},
    {"id": 2, "monto": 50.0, "tipo": "gasto"},
    {"id": 3, "monto": 30.0, "tipo": "gasto"},
    {"id": 4, "monto": 150.0, "tipo": "ingreso"}
]
Salida esperada:

{
    "total_ingresos": 350.0,
    "total_gastos": 80.0,
    "mayor_gasto": {"id": 2, "monto": 50.0, "tipo": "gasto"}
}
Criterios de Evaluación
Lógica correcta y funcional.
Código limpio, legible y con nombres descriptivos.
Uso eficiente de estructuras de datos y librerías estándar de Python.
Capacidad para trabajar con datos estructurados (dictionaries y lists).
Tiempo Sugerido
60-90 minutos.