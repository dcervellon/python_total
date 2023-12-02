def devolver_distintos(n1, n2, n3):
    suma_nums = sorted([n1, n2, n3])

    if sum(suma_nums) > 15:
        return max(suma_nums)
    elif sum(suma_nums) < 10:
        return min(suma_nums)
    elif sum(suma_nums) in range(10, 16):
        return suma_nums[1]


print(devolver_distintos(3, 2, 7))
