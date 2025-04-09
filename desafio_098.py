from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1 if inicio < fim else -1
    if inicio < fim and passo < 0:
        passo = abs(passo)
    if inicio > fim and passo > 0:
        passo = -passo
    for i in range(inicio, fim +(1 if passo > 0 else -1), passo):
        print(i , end=' ')
        sleep(0.5)
    print('FIM!')
    print()
    print('-'*25)   


print('-'*25)
print('Contagem de 1 até 10 de 1 em 1')
contador(0, 10, 1)

print('Contagem de 10 até 1 de 2 em 2')
contador(10, 0, -2)


print('Agora é a sua vez!')
inicio = int(input('Qual é o inicio? '))
fim = int(input('O fim? '))
passo = int(input('E o passo? '))
contador(inicio, fim, passo)
print()