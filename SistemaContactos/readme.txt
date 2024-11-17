Ejercicio: Sistema de Gestión de Contactos
Crea una aplicación en Python que gestione una lista de contactos.

Cada contacto tiene las siguientes propiedades:
    Nombre
    Apellido
    Teléfono
    Email
Objetivo del programa: 
    poder agregar, eliminar, modificar y mostrar los contactos. La información de cada contacto debe guardarse en un archivo llamado contactos.txt y cargarse desde el archivo cada vez que se inicia el programa.

Requerimientos:
    Clase Contacto: 
        Define una clase Contacto con las propiedades mencionadas (nombre, apellido, teléfono, email) y un método para mostrar la información de manera ordenada.

Clase AgendaContactos:
    Debe contener una lista de objetos Contacto.
    Métodos:
        agregar_contacto(): Recibe un objeto Contacto y lo añade a la lista.
        eliminar_contacto(): Permite eliminar un contacto mediante el nombre o índice.
        modificar_contacto(): Permite modificar un contacto por nombre.
        mostrar_contactos(): Muestra todos los contactos en la lista.
Manejo de Archivos:

Al iniciar el programa, debe verificar si existe el archivo contactos.txt. Si no existe, debe crearlo vacío.
Al agregar o modificar un contacto, actualiza la lista de contactos en el archivo.
Al mostrar contactos, lee la lista desde el archivo.
Interfaz del Programa:

Presenta un menú al usuario con opciones:
    1. Agregar contacto
    2. Eliminar contacto
    3. Modificar contacto
    4. Mostrar todos los contactos
    5. Salir
Implementa control de errores para validar que el email tenga un formato correcto y que el número de teléfono sea numérico.

Opcional (Desafío Extra):
    Implementa un método de búsqueda que permita buscar contactos por nombre o apellido.
    Agrega una opción en el menú para exportar los contactos a un archivo csv
    