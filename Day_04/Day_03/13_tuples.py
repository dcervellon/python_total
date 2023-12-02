# En Python, una tupla es una estructura de datos similar a una lista, pero a diferencia de las listas, las tuplas son inmutables. Esto significa que una vez que se crea una tupla, sus elementos no pueden ser modificados, añadidos o eliminados. Las tuplas se utilizan para representar colecciones de elementos que no deben cambiar.

# Para crear una tupla, puedes usar paréntesis () y separar los elementos con comas. Aquí tienes ejemplos de cómo trabajar con tuplas en Python:

my_tuple = (1, 2, 3, 4)
print(type(my_tuple))


# Puedes acceder a los elementos de una tupla utilizando índices, al igual que en las listas. Los índices comienzan en 0:

primer_elemento = my_tuple[0]  # Accede al primer elemento (1)
segundo_elemento = my_tuple[1]  # Accede al segundo elemento (2)


# Puedes desempaquetar una tupla asignando sus elementos a variables individuales:

a, b, c, d = my_tuple  # a = 1, b = 2, c = 3, d = 4


# Concatenación de tuplas:
# Puedes concatenar tuplas utilizando el operador +:

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
concat_tuple = tuple1 + tuple2
print(concat_tuple)
