t = mais = vmenor = 0
menor = ''
primeiro = True 
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    t += preço
    if preço > 1000:
        mais += 1 
    if primeiro or preço < vmenor:
        menor = produto
        vmenor = preço
        primeiro = False
    continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('FIM')
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} que custa R${vmenor:.2f}')
