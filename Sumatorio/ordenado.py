class OperacionInvalidaError(Exception):
    """Excepción personalizada para operaciones no válidas."""
    pass

class Sumatorio():
    def __init__(self):
        self.result = ""

    def get_numb(self):
        while True:
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                return a, b
            except ValueError:
                print("Error: Por favor, ingresa un número válido.")

    def sumar(self, a, b):
        self.result = a + b
        print("Resultado:", self.result)
    
    def resta(self, a, b):
        self.result = a - b
        print("Resultado:", self.result)

    def multi(self, a, b):
        self.result = a * b
        print("Resultado:", self.result)
    
    def divi(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Error: No se puede dividir por cero.")
        self.result = a / b
        print("Resultado:", self.result)

def main():
    s = Sumatorio()
    while True: 
        try:
            a, b = s.get_numb()
            operacion = input("Selecciona una de estas opciones ->  + , - , * , /\n")
            if operacion == "+":
                s.sumar(a, b)
            elif operacion == "-":
                s.resta(a, b)
            elif operacion == "*":
                s.multi(a, b)
            elif operacion == "/":
                s.divi(a, b)
            else:
                raise OperacionInvalidaError(f"Operación '{operacion}' no es válida.")
        except ZeroDivisionError as e:
            print(e)
        except OperacionInvalidaError as e:
            print(e)
        except Exception as e:
            print("Ha ocurrido un error:", e)
        
        repetir = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()
