from products import products

def prod():
    for prods in products:
        print(prods['id'])
    return prods
prod()

# def new_prod():
#     title = input("Nombre: ")
#     description = input("Definicion: ")
#     done = input("Terminado: ")
#     ultimo_producto = products[-1]['id']
#     nuevo_id = ultimo_producto +1
#     nuevo_prod = {
#         'id': nuevo_id,
#         'title': title,
#         'description': description,
#         'done': done
#     }
#     products.append(nuevo_prod)
#     print(products)

# new_prod()


def kit_prod():
    print(products)
    num_elim = int(input("Introduce el id que deseas eliminar: "))  # Convertimos a entero
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

kit_prod()
prod()

