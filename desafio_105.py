def notas(* n, situação = False):
    """
    -> Função para analizar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos(aceita varias)
    :param situação: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situação:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resposta = notas(5.5, 2.5, 1.5, situação=True)
print(resposta)
#help(notas)