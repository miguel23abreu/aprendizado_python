n = int(input('digite um número qualquer: '))
print('''Escolha uma das opções: 
[ 1 ]para converter o número escolhido em binário
[ 2 ]para converter em octal
[ 3 ]para converter em hexadecimal''')
op = int(input('digite a opção que deseja: '))
if op == 1:
    print('o número {} em binário fica {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('o número {} em octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('o número {} em hexadecimal fica {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mERRO, NÚMEROS INVÁLIDOS\033[m')