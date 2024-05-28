from math import sqrt, hypot
ca = float(input('digite o cateto adjacente do triângulo retângulo: '))
co = float(input('digite o valor do cateto oposto: '))
hipo = hypot(ca, co)
print('o cateto sdjacente tem {}m e o cateto oposto {}m e a sua hipotenusa é {:.1f}m'
      .format(ca, co, hipo))
