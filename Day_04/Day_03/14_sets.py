# En Python, un conjunto (set) es una colección desordenada de elementos únicos. Los conjuntos se utilizan para almacenar valores distintos sin duplicados y son una parte fundamental de las estructuras de datos en Python. Puedes crear conjuntos utilizando llaves {} o la función set().

my_set = set([1, 2, 3, 4, 5, 'y'])
print(type(my_set), my_set)

other_set = {1, 2, 3, 4, 5, 6}
print(type(other_set), other_set)

union_sets = my_set.union(other_set)

print(union_sets)

union_sets.add('zorro')
print(union_sets)


union_sets.remove('zorro')
print(union_sets)

union_sets.clear()
print(union_sets)
