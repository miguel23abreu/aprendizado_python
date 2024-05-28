n = int(input('digite um \033[34mnúmero\033[m: '))
ne = n % 2
if ne == 0:
    print('seu número {}{}{} é par!'.format('\033[33m', n,'\033[m'))
else:
    print('seu número {}{}{} é impár!'.format('\033[33m', n,'\033[m'))
print('='*5,'FIM', '='*5)