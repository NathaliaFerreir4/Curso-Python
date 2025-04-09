from random import randint

numeros = list()
soma = 0

def sorteio():
    for _ in range(5):
        num = randint(1, 10)
        numeros.append(num)
    print(f'Sorteando 5 valores da lista: {numeros}', end=' ')
    print('PRONTO!')
def somaPar(numeros):
    soma = 0
    for n in (numeros):
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos: {soma}')

    
sorteio()
somaPar(numeros)

