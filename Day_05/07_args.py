def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(12, 66, 1, 1, 1, 1, 1))
