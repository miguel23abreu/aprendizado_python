n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
if n1 > n2:
    print('o primeiro valor é maior')
    print('o segundo valor é menor')
elif n2 > n1:
    print('o segundo valor é maior')
    print('o primeiro valor é menor')
else:
    print('Os dois valores são iguais')