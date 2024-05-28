re = 1
c = 0
while True:
    n = int(input('digite um número para a tabuada: '))
    if n < 0:
        break
    print('-=' * 20)
    while c < 11:
        c += 1
        re = n * c
        if c == 11:
            c = 0
            break
        print(f'{n} x {c} = {re}')
    print('-=' * 20)
print('programa de tabuada encerrado, volte sempre')