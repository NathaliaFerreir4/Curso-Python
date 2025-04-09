cidade = input('Qual é o nome da sua cidade? ').strip()

if cidade[:5].upper() == 'SANTO':
    print('A palavra "Santo" encontra-se no inicio')

else:
    print('A palavra "Santo" não foi encontrada no inicio da frase')