# El método split() en Python se utiliza para dividir una cadena de texto en una lista de subcadenas, utilizando un carácter (o una secuencia de caracteres) como separador. Por defecto, el separador es un espacio en blanco.

# Aquí tienes un ejemplo de cómo usar el método split():

text = "This is a new text from Mateo's book"

split_result = text.split()
print(split_result)


text2 = 'Hola, como estan todo hoy ?'
split_result2 = text2.split()
print(split_result2)
split_result2 = text2.split(' ')
print(split_result2)
split_result2= text2.split(',')
print(split_result2)
split_result2= text2.split('o')
print(split_result2)



# El método split() es útil para dividir cadenas de texto en elementos separados y trabajar con ellos por separado, como en el caso de procesar datos CSV o listas de elementos separados por comas.
