qv = 0
s = 0
for n in range(1, 7):
    n = int(input('digite o {}° número: '.format(n)))
    if n % 2 == 0:
        qv = 1 + qv
        s = s + n
print('o resultado de todos os {} valores pares é {}'.format(qv, s))
