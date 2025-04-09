salario = float(input('Digite o seu salario: '))

if salario > 1250:
    aumento = salario * 1.10
    print('O seu salario teve um aumento de 10 porcento e será: R${:.0f},00'.format(aumento))
else:
    aumento = salario * 1.15
    print('O seu salario teve um aumento de 15 porcento e será: R${:.0f},00'.format(aumento))
