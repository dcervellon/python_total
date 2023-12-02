# La función enumerate en Python se utiliza para recorrer una secuencia (como una lista, tupla o cadena) al mismo tiempo que se realiza un seguimiento del índice o posición de los elementos en la secuencia. La función enumerate devuelve un objeto iterable que genera pares de índice y valor en cada iteración. Esto es útil cuando necesitas saber tanto el valor como su posición en la secuencia.


my_lista = ["a", "b", "c", "d", "e", "f", "g"]

for index, letter in enumerate(my_lista):
    print(f"{index+1}. {letter}")


lista_nombres = ["Marcos", "Laura", "Monica", "Celia"]


for index, name in enumerate(lista_nombres):
    if name.startswith("M"):
        print(index)
