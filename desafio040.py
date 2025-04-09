n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Agora a segunda:'))
media = (n1 + n2) / 2

if media < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[34mRECUPERAÇÃO!\033[m')
else:
    print('PARABENS! Você foi \033[32mAPROVADO!\033[m')