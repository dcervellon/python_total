# El control de flujo en Python se refiere a cómo puedes dirigir el flujo de ejecución de un programa, tomando decisiones basadas en condiciones y repitiendo ciertas acciones en función de iteraciones. Los elementos principales para el control de flujo en Python son las estructuras condicionales (if, elif, else) y las estructuras de repetición (for y while). A continuación, te mostraré cómo funcionan estas estructuras:


pet = "pato"
age = 32
is_man = True
is_women = True

# 1. Estructuras condicionales:

if age > 18:
    print("Si es mayor de edad")
else:
    print("es menor de edad")


if age > 18:
    print("claro puedes pasar")
elif age == 18:
    print("los acabas de cumplir, asi no se puede")
else:
    print("no, vete de aqui antes que llame a tus padres")

# Operador ternario

print("Si es perro") if pet == "perro" else print(
    "eso es un gato u otras cosa, pero no es un perro"
)

if is_man:
    print("si es hombre")
else:
    print("al parecer es otra cosa")


if not is_women:
    print("si es mujer")
else:
    print("tiene pyp")


print("es man") if is_man else print("no es man")
