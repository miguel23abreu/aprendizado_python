def leiaint(num=0):
    print('-'*30)
    while True:
        num = str(input('digite um número: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[31mERRO DE, DIGITE UM NÚMERO INTEIRO!\033[m')
    return num


n = leiaint()
print(f'O valor digitado foi {n}')
