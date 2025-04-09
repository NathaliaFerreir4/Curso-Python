valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = str(input('Voce quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
print(len(valores))
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O valor 5 foi digitado e esta na lista!')
else:
    print('O valor 5 NÃO foi digitado!')