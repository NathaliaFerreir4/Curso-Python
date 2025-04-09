valor = [[], []]
numero = 0

for i in range(1, 8):
    numero = int(input('Digite o valor: '))
    if numero % 2 == 0:
        valor[0].append(numero)
    else:
        valor[1].append(numero)
valor[0].sort()
valor[1].sort()
print(f'Os valores impares são {valor[1]}')
print(f'Os valores pares são {valor[0]}')