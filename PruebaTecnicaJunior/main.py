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
