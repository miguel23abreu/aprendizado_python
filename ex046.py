from datetime import date
maidade = 0
meidade = 0
for c in range(1, 8):
    anc = int(input('digite o ano de nascimento da {}° pessoa: '.format(c)))
    if (date.today().year - anc) >= 18:
        maidade += 1
    else:
        meidade += 1
print('desta lista, {} pessoas são maiores de idade'.format(maidade))
print('E {} pessoas são menor de idade'.format(meidade))