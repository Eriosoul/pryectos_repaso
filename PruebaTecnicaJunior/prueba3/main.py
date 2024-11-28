class GestionInventario:
    def __init__(self):
        # Lista para almacenar productos, cada producto será un diccionario
        self.inventario = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        """
        Agrega un producto al inventario. Si el producto ya existe, actualiza la cantidad.
        """
        nombre = nombre
        categoria = categoria
        precio = precio
        cantidad = cantidad

        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad

        }

        for item in self.inventario:
            if item['nombre'] == nombre and item['categoria'] == categoria:
                item['cantidad'] += cantidad
                print(f"La cantidad del {nombre} se ha actualizado a {categoria}")
                print(self.inventario)
                break
        else:
            self.inventario.append(producto)
            print(self.inventario)

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario por su nombre.
        """
        print(f"Se procede a eliminar: {nombre}")
        prod_eliminar = False

        for index, item in enumerate(self.inventario):
            if item['nombre'].lower() == nombre.lower():
                del self.inventario[index]
                prod_eliminar = True
                print(f'Se ha eliminado el producto: {prod_eliminar}')
                break
        if not prod_eliminar:
            print("No se encontro dicho producto")
        print("Inventario: ")
        print(self.inventario)

    def buscar_por_categoria(self, categoria):
        """
        Muestra todos los productos en una categoría específica.
        """
        print(f'Productos en la categoria Electrónica: ')
        for item in self.inventario:
            if item['categoria'].lower() == categoria.lower():
                print(f'{item['nombre']}: Precio {item['precio']}, Cantidad: {item['cantidad']}')
                # nombre = item['nombre']
                # precio = item['precio']
                # cantidad = item['cantidad']
                #
                # print(f'{nombre}: Precio {precio}, Cantidad: {cantidad}')


    def producto_mas_caro(self, categoria):
        """
        Encuentra y muestra el producto más caro dentro de una categoría específica.
        """
        print(f'Productos en la categoría "{categoria}":')
        precio = 0
        producto_caro = [item for item in self.inventario if item['categoria'].lower() == categoria.lower()]
        if producto_caro:
            for item in producto_caro:
                if item['precio'] > precio:
                    precio = item['precio']
            print(precio)

    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        """
        precio = 0
        print("El valor todal del inventario es: ")
        for item in self.inventario:
            precio += item['precio'] * item['cantidad']
        print(precio)

# Punto de inicio del programa
if __name__ == "__main__":
    sistema = GestionInventario()

    # Pruebas iniciales
    sistema.agregar_producto("Laptop", "Electrónica", 1200.0, 10)
    sistema.agregar_producto("Smartphone", "Electrónica", 800.0, 15)
    sistema.agregar_producto("Silla", "Muebles", 150.0, 20)
    sistema.agregar_producto("Mesa", "Muebles", 300.0, 5)

    sistema.buscar_por_categoria("Electrónica")
    sistema.producto_mas_caro("Muebles")
    sistema.valor_total_inventario()
    sistema.eliminar_producto("Mesa")
    sistema.valor_total_inventario()