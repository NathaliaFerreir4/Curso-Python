aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'Media é igual a {aluno["media"]}')
if aluno['media'] < 5:
    print('Situação é a igual a Reprovado')
else:
    print('Situação é igual a Aprovado')