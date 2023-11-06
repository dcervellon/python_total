name = "Mateo David"
# ? Inmutabilidad de los strings
# name[0] = "M"
# print(name)
# Result
# TypeError: 'str' object does not support item assignment


# ? Concatenacion de Strings

last_name = "Cervellon Castellanos"
complete_name = name + " " + last_name
print(complete_name)


# ? Multiplicar Strings
multi = name[:2] * 10
print(multi)


# ? Multilineas en strings
poem = """
Todavía tengo casi todos mis dientes

casi todos mis cabellos y poquísimas canas

puedo hacer y deshacer el amor

trepar una escalera de dos en dos

y correr cuarenta metros detrás del ómnibus

o sea que no debería sentirme viejo

pero el grave problema es que antes

no me fijaba en estos detalles.
"""
print(poem)


# ! Revisar contenido y obtener Bool como respuesta
sentence = "Todavía tengo casi todos mis dientes"

print("tengo" in sentence)  # result True
print("oye" in poem)  # result False
print("tengo" not in poem)  # result False
print("oye" not in poem)  # result True


# ? Saber longitud de un string

longitud = len(sentence)
print(longitud)
