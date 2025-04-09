r1 = int(input('Digite o primeiro valor: '))
r2 = int(input('Digite o segundo valor: '))
r3 = int(input('Digite o terceiro valor: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As medidas formam um triangulo!')
else:
    print('As medidas NÃO formam um triangulo!')