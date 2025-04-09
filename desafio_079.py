valores = []
while True:
    num = int(input('Digite um valor: '))
    
    if num in valores:
        print('Esse numero já esta na lista! Tente outro.')
    else:
        valores.append(num)
        print('Valor adicionado')
    resp = input('Voce quer continuar? [S/N]').upper().strip()
    if resp == 'N':
        break
valores.sort()
print(valores)