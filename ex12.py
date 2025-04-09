valor = float(input('Qual é o valor do produto?'))
vfinal = valor - (valor * 5 / 100)

print('O produto que \033[31mtinha\033[m o valor de R${:.2f} passa a ter o valor de R${:.2f}, após o \033[32mdesconto\033[m'.format(valor, vfinal))