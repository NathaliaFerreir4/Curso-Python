from datetime import datetime
anoAtual = datetime.now().year
aposentadoria = 0
trabalhador = list()
categorias = dict()
categorias['nome'] = str(input('Nome: '))
categorias['idade'] = int(input('Ano de nascimento: '))
categorias['CTPS'] = int(input('Numero da trabalho[0 para nao tem]:'))
categorias['idade'] = anoAtual - categorias['idade']

if categorias['CTPS'] > 0:
    categorias['CONTRATAÇÃO'] = int(input('Qual foi o ano da contratação? '))
    categorias['salario'] = float(input('Qual é o seu salario?'))
    print(categorias)
    anos_trabalho = anoAtual - categorias['CONTRATAÇÃO']
    categorias['aposentadoria'] = categorias['idade'] + (35 - anos_trabalho)
    for c, v in categorias.items():
        print(f'{c} tem o valor de {v}')
