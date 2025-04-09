c = ('\033[m',    # 0 - Sem cor
     '\033[31m',  # 1 - Vermelho
     '\033[32m',  # 2 - Verde
     '\033[34m',  # 3 - Azul
     '\033[33m',  # 4 - Amarelo
     '\033[35m')  # 5 - Roxo 
    

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='') 
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 5)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)