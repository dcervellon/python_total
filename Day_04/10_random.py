from random import *


# Generar un número entero aleatorio entre 1 y 10
numero_aleatorio = randint(1, 10)
print(numero_aleatorio)


# Generar un número decimal aleatorio entre 0 y 1
numero_aleatorio = uniform(0, 1)
print(numero_aleatorio)


opciones = ["manzana", "plátano", "naranja", "uva"]
fruta_aleatoria = choice(opciones)
print(fruta_aleatoria)


cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
shuffle(cartas)
print(cartas)
