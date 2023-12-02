# El método join() en Python se utiliza para unir una lista de cadenas de texto en una sola cadena, utilizando una cadena separadora como "pegamento". Este método es útil cuando deseas combinar elementos de una lista en una única cadena y especificar cómo se deben separar estos elementos.

# El método join() se llama en una cadena que actúa como el separador y recibe como argumento una lista de cadenas que deseas unir. Aquí tienes un ejemplo:

fruits = ["apple", "pear", "kiwi"]
string_join = ', '.join(fruits)
print(string_join)
