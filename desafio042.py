a = float(input('Digite o primeiro valor:'))
b = float(input('O segundo valor:'))
c = float(input('O ultimo valor:'))

if a < b + c and b < a + c and c < a + b:
    print('É UM TRIANGULO')
    if a == b and b == c and c == a:
        print('Equilátero')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Não é um triangulo!')