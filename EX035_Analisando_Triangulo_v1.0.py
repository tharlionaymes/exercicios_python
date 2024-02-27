# EXERCÍCIO 035 - Analisando Triângulo v1.0

linha = '-=-' * 20
titulo = 'ANALISANDO TRIÂNGULO v1.0'

print(linha)
print(titulo.center(60))
print(linha)

print('\nVocê deverá digitar 3 números (RETAS)!')

a = float(input('\nDigite a primeira reta: '))
b = float(input('\nDigite a segunda reta: '))
c = float(input('\nDigite a terceira reta: '))


if (abs(b - c) < a < (b + c ) and abs(a - c) < b < (b + c ) and abs(a - b) < c < (b + c )) == True:
    print('Essas 3 retas PODEM formar um TRIÂNGULO!!!')

else:
    print('Essas 3 retas NÃO podem formar um TRIÂNGULO!!!')
