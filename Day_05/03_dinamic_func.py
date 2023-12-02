def check_3_cifras(num):
    return num in range(100, 1000)


result1 = check_3_cifras(120)
result2 = check_3_cifras(12000)


lista_numeros = [122, 55, 30, 788, 10, 33, 67]


def check_list(lista_n):
    tres_cifras_list = []
    for n in lista_n:
        if n in range(100, 1000):
            print(n)
            tres_cifras_list.append(n)
    return tres_cifras_list


result3 = check_list(lista_numeros)
print(result3)
