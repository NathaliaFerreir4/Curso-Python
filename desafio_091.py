from random import randint
from time import sleep
from operator import itemgetter
sorteados = {'jogador1': randint(1,6),
             'jogador2': randint(1,6),
             'jogador3': randint(1,6),
             'jogador4': randint(1,6)
             }
ranking = list()
print('Valores sorteados: ')
for i, v in sorteados.items():
    print(f'{i} tirou {v} no dado')
    sleep(1)
ranking = sorted(sorteados.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)


