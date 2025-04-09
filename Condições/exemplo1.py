n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2) / 2
print('A sua nota media foi {:.1f}'.format(n))
print('PARABENS, VOCE PASSOU!' if n >= 6 else 'ESTUDE MAIS!')
