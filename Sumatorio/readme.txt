Ejercicio: Simulador de Máquina de Operaciones Básicas con Captura de Excepciones
Desarrolla un programa en Python que simule una "máquina" capaz de realizar operaciones aritméticas simples entre dos números. 
El programa debe incluir captura de excepciones para manejar posibles errores.

Objetivos del Ejercicio
    Pedir al usuario dos números.

Crea una función captura_entrada(mensaje) que solicite al usuario un número.
    Si el usuario ingresa algo que no es un número, captura el error y pide nuevamente la entrada.
    Solicitar la operación deseada.

Pregunta al usuario qué operación desea realizar: suma, resta, multiplicación o división.
    Usa un símbolo ('+', '-', '*', '/') para indicar la operación.
    Realizar la operación y manejar errores.

Define una función calcular(a, b, operacion) que:
Reciba dos números (a y b) y una operación.
Realice la operación seleccionada.
Si la operación es una división, verifica que b no sea cero. Si b es cero, genera un error y muestra un mensaje adecuado.
Si el usuario ingresa una operación no válida, lanza una excepción personalizada.
Excepciones Personalizadas y Mensajes de Error:

Crea una excepción personalizada OperacionInvalidaError para operaciones no reconocidas.
Muestra mensajes específicos para cada tipo de error (por ejemplo, "No se puede dividir entre cero" o "Operación no válida").
Bucle de Ejecución:

Muestra un menú de opciones que se repite hasta que el usuario decida salir.
Después de cada operación, pregunta al usuario si quiere realizar otra.
Si no desea continuar, el programa debe finalizar.
Recomendaciones
Estructura tu código en funciones para facilitar la lectura y la reutilización.
Maneja los errores específicos con try-except, e imprime mensajes claros que indiquen al usuario qué ha fallado.
Incluye mensajes de entrada y salida para mejorar la interacción con el usuario