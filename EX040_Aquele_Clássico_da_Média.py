# EXERCÍCIO 040 - Aquele Clássico da Média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média é {media}, você está REPROVADO')

elif 5.0 <= media <= 6.9:
    print(f'Sua média é {media}, você está de RECUPERAÇÃO')

else:
    print(f'Sua média é {media}, PARABÉNS você está APROVADO')
