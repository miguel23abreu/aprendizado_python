from lib.interface import *
from lib.arquivo import *
arq = 'pessoas.txt'
if not fileisTrue(arq):
    newfile(arq)
cabecalho('SISTEMA DE CADASTRO v 1.0')
while True:
    reposta = menu(['PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if reposta == 1:
        readfile(arq)
    elif reposta == 2:
        cabecalho(f'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif reposta == 3:
        fim('ENCERRANDO PROGRAMA')
        break
    else:
        print(f'\033[31mNÚMER0 INVÁLIDO\033[m')