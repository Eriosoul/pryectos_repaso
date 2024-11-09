class OperacionInvalidaError(Exception):
    """Excepción personalizada para operaciones no válidas."""
    pass

def main():
    print("Sumatorio: ")
    while True:
        try:
            a: int = input("Introduce el primer numbero: ")
            b: int = input("Introducce el segundo numero: ")
            operacion: str = input("Seleciona una de estas opciones ->  + , - , * , /\n")
            if operacion == "+":
                return a + b
            elif operacion == "-":
                return a - b
            elif operacion == "*":
                return a * b
            elif operacion == "/":
                if b == 0:
                    raise ZeroDivisionError("No se puede dividir por 0")
                return a / b
            else:
                raise OperacionInvalidaError(f"Operacion {operacion} no es valida")
            
        except ValueError:
            print("The input was not a valid integer.")
        except ZeroDivisionError as e:
            print(e)
        except OperacionInvalidaError as e:
            print(e)
        except Exception as e:
            print("Ha occurido un error", e)

        repetir = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()