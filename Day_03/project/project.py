import os
from termcolor import colored, cprint

user_text = ""
letters = []
contador = 1


def clean_console():
    os.system("clear")


def presentation():
    print("\n")
    cprint("**** Analizador de Texto 3Mil ****", "red", "on_yellow", attrs=["bold"])
    print("\n")


# Request text from user to analyze
clean_console()
presentation()

user_text = input(
    colored("\nPorfavor ingresa un texto para analizar: ", "yellow", attrs=["bold"])
).lower()


# request 3 letters to begin analysis
clean_console()
presentation()
print(colored("Ingresa 3 letras para comenzar con analisis: ", "cyan", attrs=["bold"]))
while len(letters) < 3:
    letras = input(colored(f"L = ", "green"))

    letters.append(letras.lower())


clean_console()
presentation()
print(colored("Texto del Usuario:", "red", "on_yellow", attrs=["bold"]))
print(colored(f'"{user_text}"', "cyan", attrs=["bold"]))
print(colored("Letras del Usuario:", "red", "on_yellow", attrs=["bold"]))
print(
    colored(
        f"L1: {letters[0]}, L2: {letters[1]}, L3: {letters[2]}", "cyan", attrs=["bold"]
    )
)
print("\n")


#
def count_repeated(text, letters):
    print(
        colored(
            f'En esta texto la letra "{letters[0]}" se repite: {text.count(letters[0])} veces.',
            "red",
        )
    )

    print(
        colored(
            f'En esta texto la letra "{letters[1]}" se repite: {text.count(letters[1])} veces.',
            "magenta",
        )
    )

    print(
        colored(
            f'En esta texto la letra "{letters[2]}" se repite: {text.count(letters[2])} veces.',
            "green",
        )
    )


def count_words(text):
    word_text = text.split()
    print("\n")
    print(colored(f"Este texto continen {len(word_text)} palabras.", "blue"))


def index_letters(text):
    first_letter = text[0]
    last_letter = text[-1]

    print("\n")
    print(
        colored(
            f"La primera letra de este texto es: {first_letter}",
            "yellow",
            attrs=["bold"],
        )
    )
    print(
        colored(
            f"La ultima letra de este texto es: {last_letter}",
            "yellow",
            attrs=["bold"],
        )
    )


def reverse_text(text):
    print("\n")
    reverse_order = " ".join(text.split()[::-1])

    print(
        colored("Asi quedaria el texto invertido: ", "white", "on_red", attrs=["bold"])
    )
    print(colored(f"{reverse_order}", "yellow"))

    print("\n")

    if "python" in text:
        print(
            colored(
                f'La palabra "python" Si esta en este texto',
                "white",
                "on_green",
                attrs=["bold"],
            )
        )
    else:
        print(
            colored(
                'La palabra "python" no esta en este texto',
                "white",
                "on_red",
                attrs=["bold"],
            )
        )


count_repeated(user_text, letters)
count_words(user_text)
index_letters(user_text)
reverse_text(user_text)
