m1 = float(input('digite a primeira medida: '))
m2 = float(input('digite a segunda medida: '))
m3 = float(input('digite a terceira medida: '))
if m1 - m2 < m3 < m1 + m2 and m2 - m3 < m1 < m2 + m3 and m1 - m3 < m2 < m1 + m3:
    print('As medidas formam um triângulo' , end = '')
    if m1 == m2 == m3:
        print(' Equilátero')
    elif m1 != m2 != m3 != m1:
        print(' Escaleno')
    else:
        print(' Isósceles')
else:
    print('As medidas não formam um triângulo')