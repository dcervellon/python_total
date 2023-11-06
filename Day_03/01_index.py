# El método index() en Python se utiliza para encontrar el índice de la primera ocurrencia de un elemento en una lista. Toma un valor como argumento y devuelve el índice de la primera aparición de ese valor en la lista. Si el valor no se encuentra en la lista, se genera una excepción ValueError.

my_text = "This is a test"
result = my_text[-2]
print(result)


my_text2 = "My David name is David"
result2 = my_text2.index("i")
print(result2)


result3 = my_text2.index("name")
print(result3)


result4 = my_text2.rindex("David")
print(result4)


my_list = [10, 20, 30, 40, 50, 60, 70]

print(my_list.index(30))


my_fruits = ["coco", "pear", "appe", "kiwi"]
print(my_fruits.index('kiwi'))
print(my_fruits[2])
