n = int(input('Digite um numero: '))
print('O numero \033[31m{}\033[m tem como seu antecessor o \033[34m{}\033[m e o seu sucessor \033[36m{}\033[m'.format(n, (n-1), (n+1)))