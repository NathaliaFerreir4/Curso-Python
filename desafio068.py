from random import randint
while True:
    maquina = randint(1, 10)
    s = 0
    n = int(input('Digite um numero: '))
    s = maquina + n
    if s % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    escolha = str(input('Faça a sua aposta [I/P]: ')).strip().upper()
    print(f'Voce jogou {n} e a maquina {maquina}. Total de {s} DEU {resultado}')
    if escolha != resultado:
        print('Você perdeu!')
        break
    else:
        print('Você venceu, vamos jogar novamente!')
print('FIM')
