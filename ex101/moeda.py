def aumentar(m=0, taxa=0, form = False):
    aum =  m + (m * taxa / 100)
    return aum if form is False else moeda(aum)


def diminuir(m=0, taxa=0, form = False):
    dim = m - (m * taxa/100)
    return dim if form is False else moeda(dim)


def dobro(m=0, form = False):
    dobr = m * 2
    return dobr if form is False else moeda(dobr)


def metade(m=0, form = False):
    met = m / 2
    return met if form is False else moeda(met)


def moeda(m=0, moeda = 'R$'):
    return f'{moeda}{m:.2f}'.replace('.',',')