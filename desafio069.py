t = m = f = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        t += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        m += 1
    elif sexo == 'F' and idade < 20:
        f += 1
    quer = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {t}')
print(f'Ao todo temos {m} homens cadastrados.')
print(f'E temos {f} mulher(es) com menos de 20 anos.')
