from termcolor import colored, cprint


greet = colored('Hello my friend\nThis is a program for generate a intelligent or comic name for a beer company.\n', 'yellow', attrs=['reverse'])

print(greet)

name01 = input(colored('Tell me a name, it can be an object, country, animal, fruit or whatever you can think of: ', 'cyan'))

name02 = input(colored('Tell me another name, it can also be an object, country, animal, fruit or whatever you can think of: ', 'red'))




print(colored(f'Great!, your beer name is: "{name01} {name02}"', 'yellow', attrs=['reverse']))




