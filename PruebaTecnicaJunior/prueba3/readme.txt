Prueba técnica: Sistema de Gestión de Inventario
Crea un programa que gestione un inventario de productos en una tienda. Cada producto tendrá las siguientes características:

Nombre del producto
Categoría
Precio
Cantidad en inventario
El programa debe incluir las siguientes funcionalidades:

Agregar un producto al inventario: Si el producto ya existe (mismo nombre y categoría), solo se debe actualizar la cantidad.
Eliminar un producto del inventario.
Buscar productos por categoría: Mostrar todos los productos de una categoría específica.
Producto más caro por categoría: Mostrar el producto más caro dentro de una categoría específica.
Calcular el valor total del inventario: Sumar el valor de todos los productos (precio * cantidad).
Restricciones:
Usa estructuras de datos como listas y diccionarios para almacenar los productos.
Usa funciones para cada operación y organiza el código en una clase llamada GestionInventario.
Plantilla de inicio:
class GestionInventario:
    def __init__(self):
        # Lista para almacenar productos, cada producto será un diccionario
        self.inventario = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        """
        Agrega un producto al inventario. Si el producto ya existe, actualiza la cantidad.
        """
        pass  # Implementar

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario por su nombre.
        """
        pass  # Implementar

    def buscar_por_categoria(self, categoria):
        """
        Muestra todos los productos en una categoría específica.
        """
        pass  # Implementar

    def producto_mas_caro(self, categoria):
        """
        Encuentra y muestra el producto más caro dentro de una categoría específica.
        """
        pass  # Implementar

    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        """
        pass  # Implementar

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
Requisitos adicionales:
Asegúrate de manejar errores como:
Intentar eliminar un producto que no existe.
Buscar productos en una categoría vacía.
Los precios y cantidades deben ser valores positivos.
Ejemplo de ejecución:
> Agregado producto: Laptop en categoría Electrónica
> Agregado producto: Smartphone en categoría Electrónica
> Agregado producto: Silla en categoría Muebles
> Agregado producto: Mesa en categoría Muebles

Productos en la categoría Electrónica:
- Laptop: Precio $1200.0, Cantidad: 10
- Smartphone: Precio $800.0, Cantidad: 15

Producto más caro en Muebles:
- Mesa: Precio $300.0

Valor total del inventario: $26500.0

Producto 'Mesa' eliminado.
Valor total del inventario: $25000.0