pessoas = list()
qnt = 0
soma = 0
media = 0
mulheres = list()
acimaMedia = list()
while True:
    individuo = {}
    individuo['nome'] = str(input('Nome: '))
    individuo['idade'] = int(input('Idade: '))
    individuo['sexo'] = str(input('Sexo [F/M]: ')).upper().strip()
    if individuo['sexo'] in 'F':
        mulheres.append(individuo['nome'])
    pessoas.append(individuo)
    soma += individuo['idade']
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
qnt = len(pessoas)
media = soma / qnt if qnt> 0 else 0
acimaMedia = [p for p in pessoas if p['idade'] > media]
qntAcima = len(acimaMedia)

print('-='*25)
print(f'O grupo tem {qnt} pessoas.')
print(f'A media de idade é: {media}')
print(f'As mulheres cadastradas foram: {", ".join(mulheres) if mulheres else "Nenhuma"} ')
print(f'Lista das pessoas acima da media: ')
if acimaMedia:
    for p in acimaMedia:
        print(f' ->Nome = {p["nome"]}; Idade = {p["idade"]} anos; Sexo = {p["sexo"]};')
else:
    print('Nenhuma pessoa possui a idade acima da media!')
