from random import *


def lanzar_dados():
    num1 = randint(1, 7)
    num2 = randint(1, 7)

    return num1, num2


numero1, numero2 = lanzar_dados()
print(type(numero1))

def evaluar_jugada(n1, n2):
    suma_dados = n1 + n2

    if suma_dados <= 6:
        print(f"la suma de tus dados es {suma_dados}. lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. tienes buenas chances.")
    elif suma_dados >= 10:
        print(f"la suma de tus dados es {suma_dados}. parece una jugada ganadora")


evaluar_jugada(numero1, numero2)
