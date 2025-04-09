jogadores = list()

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    qnt = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for i in range(qnt):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'Nn':
        break

print('-=' * 25)
print(f'{"ID":<5}{"Nome":<15}{"Gols":<20}{"Total"}')
print('-' * 50)
for i, jogador in enumerate(jogadores):
    print(f'{(i+1):<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]}')
print('-=' * 25)
while True:
    resp = input('Mostrar dados de qual jogador? [0 para parar] ').strip()
    if not resp.isdigit():
        print('ERRO! Digite um número válido.')
        continue

    resp = int(resp)
    
    if resp == 0:
        break
    elif resp < 1 or resp > len(jogadores):
        print('ERRO! Número de jogador inválido.')
    else:
        jogador = jogadores[resp - 1] 
        print(f'\nLEVANTAMENTO DO JOGADOR(A) {jogador["nome"]}:')
        for i, g in enumerate(jogador["gols"]):
            print(f'  No jogo {i+1} fez {g} gols.')
        print('-=' * 25)

print('Finalizando programa...')
