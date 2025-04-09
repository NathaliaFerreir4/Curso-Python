n = cont = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'soma = {s}')
print(f'quantidade de algarismos = {cont}')
