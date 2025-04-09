frase = str(input('Digite uma frase:')).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('É um palindromo!')
else:
    print('NÃO é um palindromo')
