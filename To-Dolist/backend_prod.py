from products import products

class MiProducts:
    def __init__(self) -> None:
        self.prod = products

    def see_products(self):
        print(self.prod)

    def new_prod(self):
        title = input("Nombre: ")
        description = input("Definicion: ")
        done = input("Terminado: ")
        ultimo_producto = products[-1]['id']
        nuevo_id = ultimo_producto +1
        nuevo_prod = {
            'id': nuevo_id,
            'title': title,
            'description': description,
            'done': done
        }
        products.append(nuevo_prod)
        

    def kit_prod(self):
        print(products)
        num_elim = int(input("Introduce el id que deseas eliminar: "))  
        print(f"Ha seleccionado el {num_elim}")
        opcion = input("¿Es correcto? Y(Si)/N(no)").title()
        print(opcion)
        
        if opcion == "Y":
            for product in products:
                if product['id'] == num_elim:
                    products.remove(product)
                    print("Se elimino correctamnete el producto", product)
                    
                else:
                    print("No se encontró un producto con ese id.")
        else:
            print("No se eliminó nada")


    def upd_prod(self):
        print(products)
        num_elim = int(input("Introduce el id que deseas modificar: "))
        print(f"Ha seleccionado el {num_elim}")
        opcion = input("¿Es correcto? Y(Si)/N(no)").title()
        print(opcion)
        
        if opcion == "Y":
            for product in products:
                if product['id'] == num_elim:
                    title = input("Nombre producto: ")
                    description = input("Descripcion del producto: ")
                    done = input("Terminado: ")
                    
                    prod_upd = {
                        'id': product['id'],
                        'title': title,
                        'description': description,
                        'done': done
                    }
                    product.update(prod_upd)
                    print("Se modificó correctamente el producto", product)
                    encontrado = True  
                    break 

            if not encontrado:  
                print("No se encontró un producto con ese id.")
        else:
            print("No se modifico nada")

def menu():
    m: MiProducts = MiProducts()
    while True:
        print("Menu: ")
        print("1. Ver productos")
        print("2. Añadir producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        option = int(input("Seleciona una opcion: "))
        if option == 1:
            m.see_products()
        elif option == 2:
            m.new_prod()
        elif option == 3:
            m.upd_prod()
        elif option == 4:
            m.kit_prod()
        elif option == 5:
            print("Adio")
            break
        else:
            print("Comando no reconocido")
        

if __name__ == "__main__":
    menu()  