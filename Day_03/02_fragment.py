# En Python, el método "slice" no es un método en sí, sino una técnica para acceder a una porción (subconjunto) de una secuencia, como una cadena (string), una lista o una tupla. Los "slices" se crean utilizando la notación de índices y tienen la forma secuencia[inicio:fin].

# inicio: Este valor especifica el índice a partir del cual comienza el slice. El elemento en este índice está incluido en el slice.

# fin: Este valor especifica el índice en el que termina el slice. El elemento en este índice no está incluido en el slice.


text = "ABCDEFGHIJKLMNOPQRSTUV"
fragment = text[2]
print(fragment)
# result "C"


fragment = text[2:5]
print(fragment)
# result "CDE"

fragment = text[2:12:2]
print(fragment)
# result "CEGIK"

fragment = text[3:]
print(fragment)
# result "DEFGHIJKLMNOPQRSTUV"

fragment = text[0::2]
print(fragment)
# result  "ACEGIKMOQSU"

fragment = text[::3]
print(fragment)
# result "ADGJMPSV"

fragment = text[::-1]
print(fragment)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener una porción de la lista desde el índice 2 al índice 5 (inclusive)
sub_list = my_list[2:6]
print(sub_list)
# sub_lista contendrá [2, 3, 4, 5]

# Obtener una porción desde el principio de la lista hasta el índice 3
sub_list = my_list[:4]
print(sub_list)
# sub_lista contendrá [0, 1, 2, 3]

# Obtener una porción desde el índice 6 hasta el final de la lista
sub_list = my_list[6:]
print(sub_list)
# sub_lista contendrá [6, 7, 8, 9]

# Copiar la lista completa (realizar un "shallow copy")
copy_list = my_list[:]
print(copy_list)
# copia_lista contendrá una copia exacta de my_list
