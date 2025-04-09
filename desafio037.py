numero = int(input('Digite um numero inteiro: '))
conversao = int(input('Para conversao, digite 1 para binario, 2 para octal ou 3 para hexadecimal.'))

if conversao == 1:
    print('O numero {} convertido para binario é \033[33m{}\033[m'.format(numero, (bin(numero)[2:])))
elif conversao == 2:
    print('O numero {} convertido para octal é \033[33m{}\033[m'.format(numero, (oct(numero)[2:])))
elif conversao == 3:
    print('O numero {} convertido para hexadecimal é \033[33m{}\033[m'.format(numero, (hex(numero)[2:])))
else:
    print('Digite uma opção válida!')