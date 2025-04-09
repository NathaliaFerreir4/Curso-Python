velocidade = int(input('Qual é a velocidade do carro?'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Permaneça nesta velocidade, caso contrario você será multado se passar de 80km/h')
else:
    print('Voce foi multado por excesso de velocidade! O valor da multa é: R${},00'.format(multa))