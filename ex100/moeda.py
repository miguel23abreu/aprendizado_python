def aumentar(m=0, taxa=0):
    aum =  m + (m * taxa / 100)
    return aum


def diminuir(m=0, taxa=0):
    return m - (m * taxa/100)


def dobro(m=0):
    return m * 2


def metade(m=0):
    return m / 2


def moeda(m=0, moeda = 'R$'):
    return f'{moeda}{m:.2f}'.replace('.',',')
