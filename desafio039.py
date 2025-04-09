from datetime import datetime

nascimento = int(input('Digite o ano do seu nascimento:'))
idade = (datetime.now().year) - nascimento

if idade < 18:
    print('Você ainda irá se alistar ao serviço militar!Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Esta na hora de se alistar ao serviço militar!')
else:
    print('Você passou do tempo de se alistar! Passara-se {} anos'.format(idade - 18))
