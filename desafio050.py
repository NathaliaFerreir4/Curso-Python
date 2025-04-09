s = 0
for i in range(0, 6):
    numero = int(input('Digite um numero:'))
    if numero % 2 == 0:
        s += numero
print('A soma dos numeros digitas é igual a {}'.format(s))