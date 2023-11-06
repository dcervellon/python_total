from termcolor import colored

#  En Python, una lista es un tipo de dato que se utiliza para almacenar una colección ordenada de elementos. Las listas son mutables, lo lo que significa que puedes agregar, eliminar y modificar elementos dentro de ellas. Las listas se definen utilizando corchetes [] y los elementos se separan por comas.


# ? Create a list
print("### Create a List ###")
empty_list = []
print(colored(f"empty_list = {empty_list}", "yellow"))
my_list = ["a", "b", "c", "d"]
print(colored(f"my_list = {my_list}", "blue"))
other_list = ["hola", 44, "43", 12.333, False, None, ["1", "3", "4"]]
print(colored(f"other_list = {other_list}", "cyan"))
print("\n")


# ? Acces to list items
print("### Acces to list items ###")
first_element = my_list[0]
print(first_element)
last_element = my_list[-1]
print(last_element)
portion = other_list[:5]
print(portion)
print("\n")

# ? Modify elements of a list
print("### Modify elements of a list ###")
print(other_list)
other_list[0] = "Mateo"
print(other_list)
print("\n")

# ? Add elements to list
print("### Add elements to list ###")
my_list.append("e")  # solo se puede agregar un argumento a la vez
print(my_list)
my_list.insert(1, 1)
print(my_list)
print("\n")

# ? Delete elements to list
print("### Delete elements to list ###")
other_list.pop()
other_list.pop(3)
print(other_list)
other_list.remove(44)
print(other_list)
print("\n")


# ? length of a list
print("### Dlength of a list ###")
print(len(other_list))
