n = int(input('Digite um numero:'))

print('O \033[4;31;40mdobro\033[m do numero {} é igual a {}, o \033[4;32;40mtriplo\033[m {} e a sua \033[4;33;40mraiz quadrada\033[m {:.0f}'.format(n, (n*2), (n*3), pow(n, 1/2)))