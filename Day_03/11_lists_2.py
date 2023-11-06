list = ["hola", 44, "43", 12.333, False, None, ["1", "3", "4"], "ZZ", 231]
letters = ["f", "h", "z", "a", "p", "r", "m", "s"]
# sort(): Ordena los elementos de la lista en orden ascendente (para listas de números) o alfabético (para cadenas).

letters.sort()
print(letters)

# ! Tomar nota que el metodo sort no puede ser guardado en una variable, si no mas bien se ejecuta en el lugar


new_list = ["a", "f", "j", "p", "y", "e"]

# En Python, el método reverse() se utiliza para invertir el orden de los elementos en una lista. Este método modifica la lista original en su lugar y no crea una nueva lista invertida. Aquí tienes un ejemplo de cómo usar el método reverse():

new_list.reverse()
print(new_list)
