
        t2 = valor // 20
        print(f'Toral de {t} notas de R$20')
    elif valor >= 10:
        t3 = valor // 10
        print(f'Total de {t3} notas de R$10')
    else:
        t4 = valor / 1
        print(f'Total de {t4} cedulas de R$1')
    break
print('Volte sempre!')