valor = float(input('Qual é o valor do imovel?'))
salario = float(input('Qual é o seu salario?'))
prazo = int(input('Em quantos anos voce irá pagar?'))
emprestimo = valor / (prazo * 12)
#porcentagem = emprestimo * 0.3

if emprestimo <= 0.3 * salario:
    print('Parabens! Emprestimo aprovado.')
else:
    print('Infelizmente o seu emprestio nao foi aprovado!')