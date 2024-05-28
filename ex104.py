def leiaint(num=0):
    #print('-'*30)
    while True:
        try:
            num = int(input('Número inteiro: '))
        except Exception as erro:
            print(f'\033[31mERRO {erro.__class__}, DIGITE UM NÚMERO INTEIRO!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mO usuario não informou o dado\033[m')
            return 0
        else:
            return num


def leiafloat(num=0):
    while True:
        try:
            num = float(input('Número real: '))
        except Exception as erro:
            print(f'\033[31mERRO {erro.__class__},DIGITE UM NÚMERO REAL!\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mO usuario não informou o dado\033[m')
            return 0
        else:
            return num


inteiro = leiaint()
real = leiafloat()
print(f'O valor inteiro digitado foi {inteiro} e p valor ral digitado foi {real}')