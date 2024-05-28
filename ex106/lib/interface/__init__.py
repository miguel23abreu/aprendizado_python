def leiaint(num):
    #print('-'*30)
    while True:
        try:
            num = int(input(f'{num}'))
        except Exception as erro:
            print(f'\033[31mERRO {erro.__class__}, DIGITE UM NÚMERO INTEIRO!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mO usuario não informou o dado\033[m')
            return 0
        else:
            return num


def linha(tam=35):
    return '='* tam


def cabecalho(txt):
    print(linha())
    print(txt.center(35))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for it in lista:
        print(f'\033[33m{c}\033[m - \033[34m{it}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua opção:\033[m ')
    return opc

def fim(f):
    from time import sleep
    print(linha())
    print(f, end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(0.4)
    print('VOLTE SEMPRE')
    print(linha())

