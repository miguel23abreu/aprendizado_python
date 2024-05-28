import random
n1 = str(input('primeira pessoa: '))
n2 = str(input('segunda pessoa: '))
n3 = str(input('terceira pessoa: '))
n4 = str(input('a quarta pessoa: '))
pessoas = [n1, n2, n3, n4]
random.shuffle(pessoas)
print('a ordem de quem vai apresentar os trabalhos vai ser .' )
print(pessoas)