no1 = float(input('quanto foi a primeira nota? '))
no2 = float(input('quanto foi a segunda nota? '))
cores = {'limpa':'\033[m' , 'vermelho':'\033[31m'}
media = (no1 + no2) / 2
if media < 5.0:
    print('a sua média foi {:.1f} e {}Você foi reprovado{}, no próximo ano estude mais!'.format(media, cores['vermelho'], cores['limpa']))
elif media <= 6.9:
    print('a sua média foi {:.1f} e você foi para a recuperação, ainda tem chance de passar!'.format(media))
else:
    print('a sua média foi {:.1f} e você foi aprovado, meus parábens!'.format(media))
