valores = []
impares = []
pares = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')