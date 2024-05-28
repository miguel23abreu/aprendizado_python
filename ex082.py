aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de notas do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
print('=-'*30)
print('>>Fim do programa<<')