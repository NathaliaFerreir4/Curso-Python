valores = []
for i in range(3):
    linha = []
    for p in range(3):
        numero = int(input(f'Digite um valor para {i, p}: '))
        linha.append(numero)
    valores.append(linha)
for linha in valores:
    print(linha)
