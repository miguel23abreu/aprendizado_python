print(6*'=', 'ánalise de triângulos', 6*'=')
r1 = float(input('qual a medida da primeira reta? '))
r2 = float(input('qual a medida da segunda reta? '))
r3 = float(input('qual a medida da terceira reta? '))
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('é possível formar um \033[1;31mtriângulo\033[m')
else:
    print('não é póssivel formar um \033[1;31mtriângulo\033[m')

