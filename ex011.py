from random import choice
a1 = input('digite o nome do primeiro aluno: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print('será realizado um sorteio com esses 4 alunos e 1 deles será sorteado.'
      '\ne o aluno sorteado foi {}'.format(escolhido))
