import os

class ListaTareas():
    def __init__(self):
        self.tareas = []
        self.directorio = "ListaDeTareas/data/"
        self.file = os.path.join(self.directorio, "tareas.txt")

    def check_file(self):
        try:
            with open(self.file, 'r') as file:
                print("El archivo existe.")
                self.cargar_tareas()
        except FileNotFoundError:
            print("El archivo no existe.")
            self.create_file()

    def create_file(self):
        try:
            print("Creando el archivo...")
            with open(self.file, "x") as file:
                pass  
            print("Archivo creado.")
        except Exception as e:
            print(f"Ha ocurrido un error al crear el archivo: {e}")

    def cargar_tareas(self):
        try:
            if os.path.getsize(self.file) == 0:
                print("El archivo está vacío.")
                return
            with open(self.file, 'r') as f:
                self.tareas = [line.strip() for line in f]
                print("Tareas cargadas:", self.tareas)
        except Exception as e:
            print(f"Error al cargar tareas: {e}")
    
    def agregar_tarea(self, tarea):
        file = open(self.file, 'a')
        file.write(tarea + "\n")
        print("Tarea agegada")

    def ver_tareas(self):
        try:
            with open(self.file, 'r') as file:
                print("Lista de Tareas:")
                for i, tarea in enumerate(file, start=1):
                    print(f"{i}. {tarea.strip()}")
        except FileNotFoundError:
            print("No hay archivo de tareas para mostrar.")
    
    def actualizar_tarea(self, indice, nueva_tarea):
        try:
            self.tareas[indice - 1] = nueva_tarea
            print("Tarea actualizada con éxito.")
        except IndexError:
            print("Error: Índice fuera de rango.")
    
    def eliminar_tarea(self, indice):
        try:
             # Eliminar la tarea
            tarea_eliminada = self.tareas.pop(indice - 1) 
            print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
            
            # Guardar cambios en el archivo
            with open(self.file, 'w') as f:
                for tarea in self.tareas:
                    f.write(tarea + "\n")
        except IndexError:
            print("Error: Índice fuera de rango.")

    
def main():
    l = ListaTareas()
    l.check_file()

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion == 1:
                tarea = input("Escribe la nueva tarea: ")
                l.agregar_tarea(tarea)
            elif opcion == 2:
                l.ver_tareas()
            elif opcion == 3:
                l.ver_tareas()
                indice = int(input("Selecciona el número de la tarea a actualizar: "))
                nueva_tarea = input("Escribe la tarea actualizada: ")
                l.actualizar_tarea(indice, nueva_tarea)
            elif opcion == 4:
                l.ver_tareas()
                indice = int(input("Selecciona el número de la tarea a eliminar: "))
                l.eliminar_tarea(indice)
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor selecciona entre 1 y 5.")
        except ValueError:
            print("Error: Ingresa un número válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")    

if __name__ == "__main__":
    main()
