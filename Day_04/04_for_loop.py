# ! Un bucle for en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, diccionario, rango, etc.) y ejecutar un bloque de código para cada elemento de la secuencia. Aquí tienes la sintaxis básica de un bucle for en Python:

# ! A continuación, se presentan ejemplos de bucles for en Python utilizando diferentes tipos de secuencias:

my_list = ["a", "b", "c", "d"]
counter = 0


for index, item in enumerate(my_list):
    print(f"{index+1}. {item}")
    counter += 1

print(counter)


list_name = ["pablo", "laura", "fede", "luis", "julia"]

for index, name in enumerate(list_name):
    if name.startswith("l"):
        # if name[0] == "l":

        print(f'{index+1}. {name} empiza con "L"')
    else:
        print("ok")


my_numbers = [1, 2, 3, 4, 5, 6]
my_value = 0

# ?

for num in my_numbers:
    my_value = my_value + num

print(my_value)


# !
word = "python"

for letter in word:
    print(letter)


# ?

my_duo_list = [
    [
        1,
        2,
        3,
    ],
    [4, 5, 6],
    [7, 8, 9],
]

for a, b, c in my_duo_list:
    print(a, b, c)


persons = {"nombre": "Juan", "edad": 30, "ciudad": "México"}


for clave in persons.keys():
    print(clave)

for value in persons.values():
    print(value)


for clave, value in persons.items():
    print(clave, value)


for item in persons.items():
    print(item)
