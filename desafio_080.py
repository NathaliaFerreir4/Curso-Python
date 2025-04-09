valores = []
for i in range(5):
    num = int(input('Digite um valor: '))
    if len(valores) == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {valores}')