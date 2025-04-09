def linha(tamanho = 42):
    return '-' * tamanho

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO\033[m: Por favor, digite um numero inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuario preferiu não nao digitar esse número')
            return 0
        else:
            return n

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua opção: \033[m')
    return opc    