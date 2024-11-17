import os
import re

class SGC:
    def __init__(self):
        self.name = ""
        self.proname = ""
        self.phone = 0
        self.mail = ""
        self.dir = "SistemaContactos/data/"
        self.file = os.path.join(self.dir, "contactos.txt")
        self.contact = []
    
    def file_exist(self):
        try:
            with open(self.file, 'r') as file:
                print("Fichero existe")
                self.file_is_empty()
        except FileNotFoundError as e:
            print(f"No se encontro el fichero: {e}")
            self.gen_file()
        
    def gen_file(self):
        try:
            print("Creando fichero ...")
            with open(self.file, "x") as file:
                print("Fichero creado")
        except Exception as e:
            print(f"Ocurrio un error {e}")
    
    def file_is_empty(self):
        try:
            if os.path.getsize(self.file) == 0:
                print("El archivo está vacío.")
                self.add_contact()
                return None
            else:
                self.load_file_data()
        except Exception as e:
            print(f"Ha ocurrido un error {e}")
    
    def load_file_data(self):
        try:
            with open(self.file, 'r') as f:
                self.contact = [line.strip() for line in f]
                print("Tareas cargadas:", self.contact)
                self.add_contact()
        except Exception as e:
            print(f"Error al cargar tareas: {e}")
    
    def valid_name(self):
        while True:
            try:
                self.name = input("Introduce el nombre: ").strip()
                if self.name and self.name.isalpha():  
                    return self.name
                else:
                    print("Error: el nombre no puede estar vacío ni contener números o caracteres especiales.")
            except Exception as e:
                print(f"Ha ocurrido un error al introducir el nombre: {e}")

    def valid_proname(self):
        while True:
            try:
                self.proname = input("Introduce el apellido: ").strip()
                if self.proname and self.proname.isalpha(): 
                    return self.proname
                else:
                    print("Error: el nombre no puede estar vacío ni contener números o caracteres especiales.")
            except Exception as e:
                print(f"Ha ocurrido un error al introducir el nombre: {e}")
    
    def valid_phone(self):
        while True:
            try:
                phone_input = input("Introduce el número de teléfono (9 dígitos): ").strip()
                if phone_input.isdigit() and len(phone_input) == 9: 
                    self.phone = int(phone_input)
                    return self.phone
                else:
                    print("Error: el número de teléfono debe contener solo 9 dígitos.")
            except ValueError:
                print("Error: entrada no válida. Introduce solo números.")
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")

    def valid_email(self):
        while True:
            try:
                self.mail = input("Introudce tu email: ")
                email = "my.ownsite@our-earth.org"
                valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.mail)
                if valid:
                    return self.mail
                print("Valid email address." if valid else "Invalid email address.")
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")


    def add_contact(self):
        self.name = self.valid_name()
        self.proname = self.valid_proname()
        self.phone = self.valid_phone()
        self.mail = self.valid_email()
        
        contact_info = f"{self.name},{self.proname},{self.phone},{self.mail}"
                
        try:
            with open(self.file, 'a') as f:
                f.write(contact_info + "\n")
            print("Contacto añadido exitosamente.")
            self.load_file_data()
        except Exception as e:
            print(f"Error al guardar el contacto: {e}")




if __name__ == "__main__":
    s: SGC = SGC()
    s.file_exist()