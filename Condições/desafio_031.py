distancia = float(input('Digite a distancia da viagem, em km: '))
curta = distancia * 0.5
longa = distancia * 0.45

if distancia <= 200:
    print('O valor da passagem sera R${:.0f},00'.format(curta))
else:
    print('O valor da passagem será R${:.0f},00'.format(longa))