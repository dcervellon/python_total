from termcolor import *
import os
from random import *

ia_number = randint(1, 101)
attempts_counter = 0
user_number = 0


def clean_console():
    os.system("clear")


def prensentation():
    print(
        colored(
            "\n########### DIVINER 1.0) ########### ",
            "white",
            "on_light_magenta",
            attrs=["bold"],
        )
    )
    print(colored("Try to guess the number I'm thinking ", "white", "on_magenta"))


clean_console()
prensentation()

user_name = input(
    colored("\nHello!!, What's your name ? : ", "light_yellow", attrs=["bold"])
)

clean_console()
prensentation()
print(
    colored(
        f"\nWell, {user_name}, I've thought of a number between 1 and 100, and you only have '8' tries to guess what you think the number is.\n",
        "light_cyan",
        attrs=["bold"],
    )
)


while user_number != ia_number:
    user_number = int(
        input(
            colored(f"Attemp # {attempts_counter+1}: ", "light_green", attrs=["bold"])
        )
    )
    attempts_counter += 1
    if attempts_counter == 8 and user_number != ia_number:
        print(
            colored(
                f"\nSorry {user_name}, you have exhausted all 8 attempts.",
                "white",
                "on_red",
                attrs=["bold"],
            )
        )
        print(
            colored(
                f"\nMy number was {ia_number} !!",
                "light_magenta",
                "on_light_grey",
                attrs=["bold"],
            )
        )
        break
    elif user_number > ia_number:
        print(
            colored(
                f"My number is less than {user_number}.", "light_yellow", attrs=["bold"]
            )
        )
    elif user_number < ia_number:
        print(
            colored(
                f"My number is greated > than {user_number}.",
                "light_red",
                attrs=["bold"],
            )
        )
    elif user_number == ia_number:
        print(
            colored(
                f"Congratulations, you have guessed my number and it only took you {attempts_counter} tries.",
                "dark_grey",
                "on_green",
                attrs=[
                    "bold",
                ],
            )
        )
    else:
        continue
