class GestionEstudiantesClasificacion:
    def __init__(self):
        self.estudiantes = {
            "Juan": [85, 90, 78],
            "Ana": [92, 88, 84],
            "Luis": [70, 75, 80]
        }

    def agregar_estudiantes(self):
        nombre = input("Introduce el nombre del estudiante: ")
        clasificaciones = input("Introduce las notas del estudiante, separadas por comas: ")

        # Convertir las clasificaciones a una lista de números
        clasificaciones_lista = [float(nota) for nota in clasificaciones.split(",")]

        # Agregar al diccionario
        self.estudiantes[nombre] = clasificaciones_lista
        print(f"Estudiante agregado: {nombre} -> {clasificaciones_lista}")
        print("Lista actualizada de estudiantes:", self.estudiantes)

    def calcular_promedio(self):
        try:
            nombre = input("Que estudiante quiere ver: ")
            notas = self.estudiantes[nombre]
            promedio = sum(notas) / len(notas)
            print(f'El estudiante {nombre} tiene estas {notas} y su promedio es {promedio:.2f}')
        except KeyError:
            print(f"Estudiante no encontrado: {nombre}")
        except Exception as e:
            print(f'Ocurrio un problema: {e}')

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_promedio = 0

        for nombre, notas in self.estudiantes.items():
            promedio = sum(notas) / len(notas)
            mejor_nombre = nombre
            mejor_promedio = promedio
        if mejor_nombre:
            print(f"El mejor estudiante es {mejor_nombre} con un promedio de {mejor_promedio:.2f}")
        else:
            print("No hay estudiantes registrados.")

    def eliminar_estudiante(self):
        nombre = input('Intorduce el nombre del estudiante que se va a eliminar: ')
        if nombre in self.estudiantes:
            self.estudiantes.pop(nombre)
            print(f"Estudiante {nombre} eliminado.")
        else:
            print(f"Estudiante {nombre} no encontrado.")
        print("Lista actualizada de estudiantes:", self.estudiantes)
if __name__ == '__main__':
    g = GestionEstudiantesClasificacion()
    g.agregar_estudiantes()
    g.calcular_promedio()
    g.mejor_estudiante()
    g.eliminar_estudiante()