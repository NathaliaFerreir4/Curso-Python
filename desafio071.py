n = int(input('Qual é o valor que você quer sacar? R$'))
valor = n
ced = 50 
totC = 0

while valor > 0:
    if valor >= ced:
        valor -= ced
        totC += 1
    else:
        if totC > 0: 
            print(f'Total de {totC} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totC = 0 
print('FIM')
