# EXERCÍCIO 075 - Análise de Dados em uma Tupla

num1 = 9#int(input('Digite 1º valor: '))
num2 = 2#int(input('Digite 2º valor: '))
num3 = 3#int(input('Digite 3º valor: '))
num4 = 10#int(input('Digite 4º valor: '))

num_guarda = (num1, num2, num3, num4)

contador9 = 0

print(num_guarda)

if num1 == 9:
    contador9 += 1

if num2 == 9:
    contador9 += 1

if num3 == 9:
    contador9 += 1

if num4 == 9:
    contador9 += 1

print(f'\nO número 9 apareceu {contador9}X')

if num1 == 3:
    print(f'\nO valor 3 foi digitado primeiro na 1º posição.')

if num2 == 3:
    print(f'\nO valor 3 foi digitado primeiro na 2º posição.')

if num3 == 3:
    print(f'\nO valor 3 foi digitado primeiro na 3º posição.')

if num4 == 3:
    print(f'\nO valor 3 foi digitado primeiro na 4º posição.')

print('\nOs números pares foram: ', end = '')
if num1 % 2 == 0:
    print(f'{num1},',end = ' ')
    
if num2 % 2 == 0:
    print(f'{num2},',end = ' ')
    
if num3 % 2 == 0:
    print(f'{num3},',end = ' ')
    
if num4 % 2 == 0:
    print(f'{num4}',end = ' ')
    