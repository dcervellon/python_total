def suma_absoluta(*args):
    result = 0

    for arg in args:
        result += abs(arg)
    return result


print(suma_absoluta(2,3,5,-7))
