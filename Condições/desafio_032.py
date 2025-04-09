ano = int(input('Digite o ano que você esta: '))
if ano % 100 == 0 and ano % 400 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')