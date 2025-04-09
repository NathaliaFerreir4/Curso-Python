sexo = str(input('Qual é o sexo? [F/M]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print(f'Resposta invalida!')
    sexo = str(input('Qual é o sexo? [F/M]: ')).strip().upper()
print(f'FIM')