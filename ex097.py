def notaaluno(*n, sit=False):
    """
    >> A função notaaluno tem como objetico analisar e mostrar a situação dos alunos
    :param n: Parâmetro das notas dos alunos
    :param sit: Situação do aluno (opcional)
    :return: Retorna os dados sobre o aluno
    """
    aluno = dict()
    aluno['notas'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situação'] = 'Boa'
        elif aluno['media'] >= 5:
            aluno['situação'] = 'Regular'
        elif aluno['media'] >= 4:
            aluno['media'] = 'Ruim'
        else:
            aluno['media'] = 'Péssima'
    return aluno


aluno1 = notaaluno(2.5, 10, 5.4,6.9,8, sit=True)
print(aluno1)
help(notaaluno)