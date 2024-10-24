from products import products

def prod():
    for prods in products:
        print(prods['id'])
    return prods
prod()

def new_prod():
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
    print(products)
new_prod()
