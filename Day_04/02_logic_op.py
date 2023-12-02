# En Python, los operadores lógicos se utilizan para realizar operaciones lógicas entre valores booleanos (True o False) o expresiones que se pueden evaluar como booleanas. Los operadores lógicos más comunes en Python son:

frase = "Hola mateo como estas, hoy tienes que ir a la escuela."

# and: Este operador devuelve True si ambas expresiones a su izquierda y a su derecha son True.
my_bool = 12 > 10 and 13 > 15
comparison_str = 12 == 12 and "perro" == "perro"


# or: Este operador devuelve True si al menos una de las expresiones a su izquierda o a su derecha es True.

or_bool = "hola" != "Hola" or 12 > 233

is_word = "Hola" in frase and "estas" in frase
is_word2 = "perro" in frase or "que" in frase


# not: Este operador invierte el valor de una expresión booleana. Si la expresión es True, not la convierte en False, y viceversa.

my_not_bool = not 12 == 12
my_not_bool2 = not "Hola" in frase


age = 18
message = "puede votar" if age > 18 else "no puede"
