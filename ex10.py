real = float(input('Qual reais voce possui?'))
dolar = real / 3.27
print('O valor de R${:.2f} convertido em \033[4;33mdolares\033[m é equivalente a ${:.2f}'.format(real, dolar))