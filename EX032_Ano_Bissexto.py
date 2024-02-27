#EXERCÍCIO 032 - Ano Bissexto

ano = int(input('Digite um Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O Ano Digitado é BISSEXTO')
else:
    print('NÃO é Ano BISSEXTO')
