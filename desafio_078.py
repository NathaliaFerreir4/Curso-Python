valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
menor = min(valores)
maior = max(valores)
pMenor = [i for i, v in enumerate(valores) if v == maior]
pMaior = [i for i, v in enumerate(valores) if v == menor]
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {pMaior}')
print(f'O menor valor digitado foi {menor} na posição {pMenor}')