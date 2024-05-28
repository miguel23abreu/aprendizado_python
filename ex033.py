from datetime import date
an = int(input('Em que ano nasceu o atleta? '))
id = date.today().year - an
print('O atleta tem {} anos'.format(id))
if id <= 9:
    print('categoria: MIRIM')
elif id <= 14:
    print('Catégoria: INFANTIL')
elif id <= 19:
    print('Catégoria: JÛNIOR')
elif id <= 25:
    print('Catégoria: SÊNIOR')
else:
    print('Catégoria: MASTER')