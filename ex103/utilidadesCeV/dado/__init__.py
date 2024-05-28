from ex103.utilidadesCeV import moeda

def leiadinheiro(msg):
    while True:
        d = str(input(msg)).replace(',', '.').strip()
        if d.isalpha() or d.strip() == '':
            print(f'\033[31mERRO! "{d}" não um número válido\033[m ')
        else:
            break
    return float(d)
