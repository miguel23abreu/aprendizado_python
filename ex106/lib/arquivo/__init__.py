from ex106.lib.interface import cabecalho

def fileisTrue(arquivo):
    try:
        a = open(arquivo, mode='rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def newfile(arquivo):
    try:
        a = open(arquivo, mode='wt+')
        a.close()
    except:
        print(f'\033[31mnão foi possivel criar o arquivo\033[m')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')


def readfile(arquivo):
    try:
        a = open(arquivo, mode='rt')
    except:
        print(f'\033[31mNão foi possivel ler o arquivo\033[m')
    else:
        cabecalho('PESSOS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, mode='at+')
    except:
        print(f'\033[31mHouve um erro ao cadastrar uma nova pessoa\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[31mHouve um erro ao escrever os dados\033[m')
        else:
            print(f'Novo registro de {nome} adicionado')
        finally:
            a.close()
