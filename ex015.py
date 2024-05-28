import random
num =int(random.randint(0,9999))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#num = str(input('informe um numero com 4 digitos:'))
print('analisando o número {}...'.format(num))
print('sua unidade é {} '.format(u))
print('a sua dezena é {}'.format(d))
print('a sua centena é {}'.format(c))
print('e a sua milha é {}'.format(m))