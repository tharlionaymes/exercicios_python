# EXERCÍCIO 033 - Maior e Menor Valores

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num1 > num2 and num1 > num3:
    print(f'O {num1} é o maior número dos 3 digitados.')

elif num2 > num1 and num2 > num3:
    print(f'O {num2} é o maior número dos 3 digitados.')
    
elif num3 > num1 and num3 > num2:
    print(f'O {num3} é o maior número dos 3 digitados.')

if num1 < num2 and num1 < num3:
    print(f'O {num1} é o menor número dos 3 digitados.')

elif num2 < num1 and num2 < num3:
    print(f'O {num2} é o menor número dos 3 digitados.')
    
elif num3 < num1 and num3 < num2:
    print(f'O {num3} é o menor número dos 3 digitados.')
