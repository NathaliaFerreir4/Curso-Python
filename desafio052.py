numero = int(input('Digite um numero para verificar se o mesmo é primo:'))
divisoes = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        divisoes += 1
if divisoes == 2:
    print('O numero {} é primo!'.format(numero))
else:
    print('O numero NÃO é primo!')