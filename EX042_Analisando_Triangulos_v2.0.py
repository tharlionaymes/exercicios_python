# EXERCÍCIO 042 - Analisando Triângulos v2.0

linha = '-=-' * 20
titulo = 'ANALISANDO TRIÂNGULO v2.0'

print(linha)
print(titulo.center(60))
print(linha)

print('\nVocê deverá digitar 3 números (RETAS)!')

a = float(input('\nDigite a primeira reta: '))
b = float(input('\nDigite a segunda reta: '))
c = float(input('\nDigite a terceira reta: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (b + c) and abs(a - b) < c < (b + c):
    print('\nEssas 3 retas PODEM formar um TRIÂNGULO!!!')

    if a == b == c:
        print('\nE esse triângulo será EQUILÁTERO')

    elif a == b or a == c or b == c:
        print('\nE esse triângulo será ISÓSCELES')

    elif a != b and a != c and c != b:
        print('\nE esse triângulo será ESCALENO')

else:
    print('\nEssas 3 retas NÃO podem formar um TRIÂNGULO!!!')
