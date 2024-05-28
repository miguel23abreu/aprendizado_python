import math
an = float(input('digite o ângulo que você deseje: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('o ângulo é {} o seno desse ângulo é {:.2f} '
      '\no seu cosseno é {:.2f} '
      '\ne a sua tangente é {:.2f}'.format(an, s, c, t))
