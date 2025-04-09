jogador = dict()
qnt = 0
jogador['nome'] = str(input('Nome do jogador: '))
qnt = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for i in range(qnt):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['total'] = sum(jogador['gols'])
print('-=' * 25)
for categoria, valor in jogador.items():
    print(f'O campo {categoria} tem o valor {valor}')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {qnt} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {g} gols')
print(f'Foi um total de {jogador['total']}')
