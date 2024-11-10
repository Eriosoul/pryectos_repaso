class OperacionInvalidaError(Exception):
    """Excepción personalizada para operaciones no válidas."""
    pass

class Sumatorio:
    def get_numb(self):
        """Solicita dos números al usuario y los devuelve como float."""
        while True:
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                return a, b
            except ValueError:
                print("Error: Por favor, ingresa un número válido.")

    def operar(self, operacion, a, b):
        """Realiza la operación dada en `operacion` con los números `a` y `b`."""
        operaciones = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else self.raise_zero_division_error()
        }

        if operacion not in operaciones:
            raise OperacionInvalidaError(f"Operación '{operacion}' no es válida.")
        return operaciones[operacion](a, b)
    
    def raise_zero_division_error(self):
        """Genera una excepción de división por cero."""
        raise ZeroDivisionError("Error: No se puede dividir por cero.")

def main():
    s = Sumatorio()
    while True: 
        try:
            a, b = s.get_numb()
            operacion = input("Selecciona una de estas opciones ->  + , - , * , /\n")
            resultado = s.operar(operacion, a, b)
            print("Resultado:", resultado)
        except (ZeroDivisionError, OperacionInvalidaError) as e:
            print(e)
        except Exception as e:
            print("Ha ocurrido un error inesperado:", e)
        
        repetir = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()