# EXERCÍCIO 074 - Maior e Menor Valores em Tupla


from random import randint

num = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))

#print(f'Os números gerados foram {num}')
print(f'Os números gerados foram: ', end = '')

for n in num:
    print(f'{n}', end = ' ')

print(f'\n\nO maior valor da tupla é {max(num)}')
print(f'\nO menor valor da tupla é {min(num)}')
