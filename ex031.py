from datetime import date
an = int(input('digite o seu ano de nascimento: '))
hom = str(input('você é homem ou mulher? '))
if hom == 'mulher':
    print('você não precisa se alistar')
id = date.today().year - an
if hom == 'homem':
    if id == 18:
        print('O jovem precisa se alistar este ano')
    elif id <= 17:
        print('o jovem ainda vai se alistar e falta {} anos para o ano do seu alistamento que será em {}'
              .format(id - 18, 18 + an))
    else:
        print('O jovem passou do prazo do alistamento há {} anos e era pare ele ter se alistado em {}'
              .format(id - 18, date.today().year - (id-18)))