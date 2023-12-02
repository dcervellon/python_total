# def cantidad_atributos(**kwargs):
#     result = []
#     new_set = set()

#     for key, value in kwargs.items():
#         new_set.add((key, value))


#     return list(new_set)


# print(cantidad_atributos(x=6, h=8, f=8, d=9, l=7, v=9))


def describir_persona( **kwargs):

    print('mateo')
    for key, value in kwargs.items():
        print(f'{key}, {value}')







describir_persona(ojos="azul", pelo="rosa")
