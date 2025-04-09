n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro:'))
if n1 > n2:
    print('O numero {} é o maior'.format(n1))
elif n2 > n1:
    print('O numero {} é o maior'.format(n2))
else:
    print('Não existe maior, pois os dois são iguais!')