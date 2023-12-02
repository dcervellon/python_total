def zero_repeat(*args):
    repeat_zero = False

    for arg in range(len(args) - 1):
        if args[arg] == 0 and args[arg + 1] == 0:
            repeat_zero = True
            break

    return repeat_zero


print(zero_repeat(1, 2, 3, 4, 0, 0, 7, 5, 4, 214, 1, 3))
