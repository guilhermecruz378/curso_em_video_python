def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mai snotas do alunos (aceita varias).
    :param sit: valor opcional. indicando se deve ou não mostrar a situação.
    :return: dicionarios com varias informaçoes sobre o aluno.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(10, 6.0, 4, 7, sit=True)
print(resp)