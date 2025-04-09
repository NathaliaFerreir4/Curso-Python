nome = str(input('Qual é o seu nome?'))
if nome == 'Nathalia':
    print('Que nome bonito!')
elif nome == 'Joao' or nome == 'Maria' or nome =='Ana' or nome == 'Matheus':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Guilherme Roledo':
    print('Belo nome masculino!')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))