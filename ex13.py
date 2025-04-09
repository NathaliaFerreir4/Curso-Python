salario = float(input('Qual é o seu salario atual?'))
aumento = salario + (salario * 15 / 100)

print('O seu salario, que \033[4;34mantes\033[m era R${:.2f} \033[4;32magora\033[m será R${:.2f}'.format(salario, aumento))