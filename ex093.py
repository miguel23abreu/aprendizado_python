def voto(nasc):
    """
    >> função que decide se uma pessoa não vota, vota obrigatoriamente ou vota opcionalmente
    :param nasc: data de nascimento
    :return: retornar o valor da idade e diz se o voto da pessoa é opcional,proíbido ou obrigatório
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 16 or idade == 17 or idade >= 70:
        return f'Com idade {idade}, O voto é opcioanal'
    elif idade < 16:
        return f'Com idade {idade}, Não vota'
    else:
        return f'Com idade {idade}, O voto é obrigatório'



v1 = int(input('Qual o seu ano de nascimento? '))
print(voto(v1))





