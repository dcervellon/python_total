# En Python, puedes formatear cadenas de varias maneras. Las tres formas más comunes de formatear cadenas son:

# Usando el operador % (formato antiguo):

# Este método es una forma más antigua de formatear cadenas y se utiliza con el operador %. Aquí hay un ejemplo:

# python
nombre = "Juan"
edad = 30
mensaje = "Mi nombre es %s y tengo %d años" % (nombre, edad)
print(mensaje)
# En este ejemplo, %s y %d son marcadores de posición para cadenas y enteros, respectivamente. Luego, los valores de nombre y edad se pasan como una tupla al operador % para reemplazar esos marcadores de posición en la cadena.

# Usando el método str.format():

# Este método permite formatear cadenas utilizando el método format() de la cadena. Aquí hay un ejemplo:


nombre = "Juan"
edad = 30
mensaje = "Mi nombre es {} y tengo {} años".format(nombre, edad)
print(mensaje)
# En este caso, {} son marcadores de posición que se reemplazarán por los valores proporcionados en el método format().

# Usando f-strings (cadenas f):

# A partir de Python 3.6, puedes utilizar f-strings para formatear cadenas de manera más sencilla y legible. Aquí hay un ejemplo:

nombre = "Juan"
edad = 30
mensaje = f"Mi nombre es {nombre} y tengo {edad} años"
print(mensaje)
# En las f-strings, los valores se pueden incluir directamente dentro de las llaves {} y Python los reemplazará automáticamente.

# Las f-strings son la forma más moderna y recomendada de formatear cadenas en Python, ya que son más legibles y más eficientes. Sin embargo, las otras dos opciones aún se utilizan en código heredado o en situaciones donde no se puede usar Python 3.6 o versiones posteriores.
