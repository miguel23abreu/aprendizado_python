def titulo(t):
    linha = len(t) + 2
    print('\033[44m', '-'*linha)
    print(f' {t} ')
    print('-'*linha)
    print('\033[m')

def manual(PYhelp=0):
    from time import sleep
    while True:
        PYhelp = input('MANUAL DE UMA FUNÇÃO OU BIBLIOTECA? ')
        if PYhelp.upper() == 'FIM':
            titulo('FINALIZANDO PROGRAMA...')
            sleep(2)
            break
        titulo(f'ACESSANDO O MANUAL DA FUNÇÃO {PYhelp}...')
        sleep(1)
        print('\033[41m')
        PYhelp = help(PYhelp)
    return f'PROGRAMA FINALIZADO, VOLTE SEMPRE!'


titulo('SISTEMA DE AJUDA PYhelp')
print(manual())
#help(help)