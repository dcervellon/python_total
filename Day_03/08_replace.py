# El método replace() en Python se utiliza para reemplazar todas las ocurrencias de una subcadena en una cadena de texto por otra subcadena especificada. Este método toma dos argumentos: el primero es la subcadena que deseas reemplazar, y el segundo es la subcadena con la que deseas realizar el reemplazo. El método devuelve una nueva cadena con todas las sustituciones realizadas.

example = "El método replace() en Python se utiliza para reemplazar todas las ocurrencias de una subcadena en una cadena de texto por otra subcadena Python"

new_sentence = example.replace('El', 'Donde').replace('Python', 'Java')

print(new_sentence)
