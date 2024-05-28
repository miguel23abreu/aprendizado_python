def fatorial(n=1, show=False):
    """
    >> função que calcula a fatorial do número n
    :param n: Parâmetro do valor a ser calculado a fatorial
    :param show: (opcional) Mostrar ou não mostrar a conta
    :return: Retorna o valor da fatorial de n
    """
    fact = 1
    print('-'*30)
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c != 1:
                print(end=' x ')
            elif c == 1:
                print(' = ',end='')
        fact *= c
    return fact


print(fatorial(6, True))
help(fatorial)