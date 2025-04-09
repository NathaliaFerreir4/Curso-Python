from random import choice

advinha = str(input('Escolha entre pedra, papel ou tesoura:')).upper()
opcoes = ['pedra', 'papel', 'tesoura']
jokenpo = choice(opcoes).upper()

if advinha == jokenpo:
    print('Voce ACERTOU!')
else:
    print('VOce ERROU!')
print(jokenpo)