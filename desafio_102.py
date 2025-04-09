def fatorial(num = 1, show = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} {'x' if c > 1 else '='} ', end='')
    return f 

print(fatorial(5, show=True))