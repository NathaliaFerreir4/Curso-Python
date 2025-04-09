valor = float(input('Qual é o valor do produto?'))
pagamento = int(input('Qual é a forma de pagamento? 1 - dinheiro; 2 - debito; 3 - credito 2x; 4 - credito 3x :'))

if pagamento == 1:
    print('O pagamento a vista da um desconto de 10 porcento e produto passa a valer R${}'.format(valor - (valor * 0.1)))
elif pagamento == 2:
    print('O pagamento no debido tem um desconto de 5 porcento e o produto passa a custar R${}'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('O pagamento parcelado e 2x nao possui desconto, o valor continua R${}'.format(valor))
elif pagamento == 4:
    print('O pagamento parcelado em 3x possui juros e passa a custar R${}'.format(valor * 1.20))
else:
    print('Digite uma opção válida!')