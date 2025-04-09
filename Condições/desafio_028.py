from random import randint

numero = randint(0, 5)
tentativa = int(input('Digite um numero entre 0 e 5: '))
if tentativa == numero:
    print('Voce acertou!')
else:
    print('Voce errou!')