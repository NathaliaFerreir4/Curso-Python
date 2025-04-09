from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*10)
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i} ', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor foi {maior}')

maior(2, 4, 1 , 9 , 10, 100)
maior(4, 7, 0)
maior()
maior(2, 1)
maior(8)
