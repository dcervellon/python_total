#
# todo::range en Python es una función que se utiliza para generar una secuencia de números enteros en un rango específico. Se puede usar en bucles for u otros contextos donde necesites una secuencia de números. La función range se usa comúnmente con bucles for para iterar sobre una secuencia de números en un rango determinado.


for num in range(1, 30):
    print(num)


super_lista = list(range(2, 40, 2))
print(super_lista)


suma_cuadrados = 0

for sq in range(1, 16):
    suma_cuadrados += sq **2
    print(suma_cuadrados)

print(suma_cuadrados)
