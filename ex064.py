nl = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete,', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
      'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = -1
while True:
    while not 0 <= n <= 20:
        n = int(input('digite um número que seja entre 0 e 20: '))
        if 0 > n > 20:
            print('\033[31mNÚMERO INVÁLIDO!\033[m')
    print(f'você digitou o número {nl[n]}')
    son = ' '
    while not son in 'sSnN':
        son = str(input('deseja continuar? [S/N]')).upper().strip()[0]
    if son == 'N':
        break
print('fim do programa')
