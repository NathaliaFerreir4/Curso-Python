def leiaInt():
    while True:
        entrada = input('Digite um numero inteiro'). replace(',', '.')
        
        try:
            num = int(entrada)
            return num
        except ValueError:
            print('ERRO! Digite novamente')


numero = leiaInt()
print(f'Você digitou o numero {numero}')