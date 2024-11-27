""" PARTE 1 """
def contar_palabras(text):
    text2 = text.replace(',','')
    r = text2.replace('.', '')
    char = r.lower()
    conteo_palabras = {}

    for i in char.split():
        if i in conteo_palabras:
            conteo_palabras[i] += 1
        else:
            conteo_palabras[i] = 1
    return conteo_palabras

text = "Hola mundo, hola universo."
resultado = contar_palabras(text)
print(resultado)

""" PARTE 2 """
def numeros_faltantes(lista, inicio, fin):
    print(f"La lista de los numeros: {lista}")
    r = set(range(inicio, fin +1))
    lista_set = set(lista)

    faltan = list(r - lista_set)
    return f"Los numeros faltantes: {sorted(faltan)}"
        


lista = [1, 2, 4, 6]
inicio = 1
fin = 6
faltan = numeros_faltantes(lista, inicio, fin)
print(faltan)


""" PARTE 3 """
class AnalizarTransacciones:
    def __init__(self):
        self.transacciones = [
            {"id": 1, "monto": 200.0, "tipo": "ingreso"},
            {"id": 2, "monto": 50.0, "tipo": "gasto"},
            {"id": 3, "monto": 30.0, "tipo": "gasto"},
            {"id": 4, "monto": 150.0, "tipo": "ingreso"}
        ]
    
    def total_ingresos(self):
        total = 0
        for r in self.transacciones:
            if r['tipo'] == 'ingreso':
                total += r['monto']
        print(f'El ingreso toal es: {total}')

    def total_gatos(self):
        total_gasto = 0
        for r in self.transacciones:
            if r['tipo'] == 'gasto':
                total_gasto += r['monto']
        print(f'El gasto toal es: {total_gasto}')

    def mayor_gasto(self):
        mayor_gasto = 0
        for r in self.transacciones:
            if r['tipo'] == 'gasto' and r['monto'] > mayor_gasto:
                mayor_gasto = r['monto']
        print(f'El mayor gasto es: {mayor_gasto}')


if __name__ == '__main__':
    a: AnalizarTransacciones = AnalizarTransacciones()
    a.total_ingresos()
    a.total_gatos()
    a.mayor_gasto()
        



