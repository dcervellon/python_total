import os
from termcolor import *


def clean_console():
    os.system("clear")


clean_console()
title_app = colored(
    f"\n--- EL AHORCADO ---\nIntenta Adivinar La Palabra\n",
    "light_yellow",
    "on_black",
    attrs=["bold", "blink"],
)
figure = colored(
    """   #    ******
   #  *        *
   # *          *
   # *   X  X   *
   # *    **    *
   #  *  ####  *
   #    ******\n\n
""",
    "light_yellow",
    attrs=["bold", "blink"],
)
print(title_app)
print(figure)
