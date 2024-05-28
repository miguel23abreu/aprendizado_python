from datetime import date
ano = int(input('digite um ano: caso queira saber sobre o ano atual coloque "0": '))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é bissexto'.format('\033[1;36m',ano, '\033[m'))
else:
    print('o ano {}{}{} não é bissexto'.format('\033[1;36m', ano, '\033[m'))