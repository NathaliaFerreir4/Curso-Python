soma = 0
maisvelho = 0
nomemaisv = ''
maisnova = 0
for i in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (responda com F ou M): ')).strip().upper()
    soma += idade
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomemaisv = nome
    if sexo == 'F' and idade < 20:
        maisnova += 1
    media = soma / 4
if nomemaisv:
    print('O homem mais velho se chama: {}'.format(maisvelho))
else:
    print('Não há homens no grupo')

print('A media da idade do grupo é: {}'.format(media))
print('{} mulhere(s) tem menos de 20 anos'.format(maisnova))
