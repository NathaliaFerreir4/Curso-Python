def ficha(nome: str = "desconhecido", gols: int = 0):
    print(f'O(a) jogador(a) {nome} fez {gols} gols.')
    return nome, gols


nome = str(input('Qual o nome do jogador? '))
if not nome:
    nome = "<desconhecido>"

try:
    gols = int(input(f'Quantos gols {nome} fez? '))
except ValueError:
    gols = 0

ficha(nome, gols)