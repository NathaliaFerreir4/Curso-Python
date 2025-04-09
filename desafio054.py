from datetime import datetime
ano = datetime.now().year
maior = 0
menor = 0
for i in range(1, 7):
    nascimento = int(input('Digite a data de nascimento do {}º'.format(i)))
    idade = ano - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas sao maior de idade e {} pessoas sao menores de idade'.format(maior, menor))
