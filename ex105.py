import urllib
import urllib.request
try:
    teste = urllib.request.urlopen('http://pudim.com.br/')
except:
    print(f'\033[31mNão foi possível acessar o site\033[m')
else:
    print(f'\033[33mSite acessado!\033[m')
    print(teste.read())
