def leiaInt():
    while True:
        try:
            entrada = int(input('Digite um numero inteiro: '))
            return entrada
        except (ValueError, TypeError):
            print('ERRO! Digite um nummero válido')
        except KeyboardInterrupt:
            print('O usuario não preencheu os dados')
            return 0
        
def leiaFloat():
    while True:
        try:
            entrada2 = float(input('Digite um numero real: '))
            return entrada2
        except (ValueError, TypeError):
            print('ERRO! Digite um numero válido')
        except KeyboardInterrupt:
            print('O usuario não preencheu os dados')
            return 0
        

        
inteiro = leiaInt()
real = leiaFloat()
print(f'O numero inteiro digitado foi {inteiro} e o numero real {real}')