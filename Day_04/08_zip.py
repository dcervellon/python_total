# La función zip en Python se utiliza para combinar dos o más secuencias en un solo objeto iterable, creando pares de elementos tomados de cada secuencia. Los elementos de las secuencias se combinan en tuplas y se generan en el orden en que aparecen en las secuencias de entrada. Esto es útil cuando necesitas trabajar con múltiples secuencias de datos al mismo tiempo, como listas, tuplas o cadenas.

names = ["Mateo", "David", "Liseth"]
ages = ["4", "32", "29"]
cities = ["San Pedro Sula", "La Lima", "Santa Barbara"]
indice = 0

combines = list(zip(names, ages, cities))

print(combines)

for name, age, city in combines:
    indice += 1
    print(f"{indice}. {name} tiene {age} anios y nacio en {city}")
