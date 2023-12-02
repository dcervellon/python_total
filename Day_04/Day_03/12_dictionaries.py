# En Python, un diccionario es una estructura de datos que se utiliza para almacenar pares clave-valor. Cada clave está asociada a un valor, y puedes acceder a los valores utilizando las claves. Los diccionarios son útiles cuando necesitas almacenar datos que están relacionados de manera no secuencial, y se acceden a los valores mediante una clave en lugar de un índice.

my_dic = {}
other_dic = {
    "name": "Mateo",
    "last_name": "Cervellon",
    "age": 4,
    "hobbie": "play videogames",
}

# Puedes acceder a los valores del diccionario utilizando las claves correspondientes:

print(other_dic)
name = other_dic["name"]
print(name)
print(type(name))
last_name = other_dic["last_name"]

new_dic = {
    "name": "david",
    "last_name": "cervellon",
    "age": 32,
    "cars": ["honda civic", "lambo"],
    "coworkers": [
        {"name": "david mejia", "position": "programmer"},
        {"name": "mario cruz", "position": "programmer"},
    ],
    "other": {"c1": "v1", "c2": "v2"},
}

print(new_dic["name"])
print(new_dic["cars"][1])
print(new_dic["coworkers"][0]["name"])
print(new_dic["other"]["c2"])


# exercise
dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())


# Agregar elementos a un diccionario

new_dic["other2"] = {1: "vaca", 2: "toro"}
print("###################")
print(new_dic)


# Sobreescribir un valor en diccionarios

new_dic["cars"][1] = "Mercedes benz"
print(new_dic)


# Acceder solo a las claves de un diccionario

keys_dic = new_dic.keys()
print(keys_dic)


# Acceder solo a los valores de un diccionari
values_dic = new_dic.values()
print(values_dic)

# Acceder a todos los item de un diccionario
items_dic = new_dic.items()
print(items_dic)


if "name" in new_dic:
    print('la llave "name" si existe en este diccionario')

del new_dic["coworkers"][1]
print(new_dic)
