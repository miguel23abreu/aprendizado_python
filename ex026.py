s = float(input('Qual o salário do fúncionario?R$ '))
if s > 1250:
    sa = s + (s*10/100)
else:
    sa = s + (s*15/100)
print('O salário do funcionario passará de R$\033[33m{:.2f}\033[m para R$\033[4;34m{:.2f}\033[m '.format(s, sa))