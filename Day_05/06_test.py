from random import *

lista_numeros = [1, 4, 8, 66, 30, 4]


def lanzar_modena():
    cara_moneda = ["Cara", "Cruz"]

    resultado_moneda = choice(cara_moneda)
    return resultado_moneda


def1 = lanzar_modena()


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruira")
        lista = []
        return lista
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista


print(probar_suerte(def1, lista_numeros))


nueva_lista = [1, 7, 3, 4, 3, 1]
todo = nueva_lista.clear()
print(todo)
