"""# EXERCÍCIO 052 - Números Primos

num_digitado = int(input('Digite um número inteiro: '))

if num_digitado >= 1 and num_digitado % 1 == 0 and num_digitado % num_digitado == 0 and num_digitado % 2 != 0 and num_digitado % 3 != 0 and num_digitado % 5 != 0 and num_digitado % 7 != 0:
	print(f'O {num_digitado} é PRIMO.')
	
else:
	print('NÃO é um número primo.')
    
    """
    

contar = 0

print('Os números primos são:')

for n in range (2, 100):
    if n <=1:
        continue

    elif n > 2 and n % 2 == 0:
        continue
    
    elif n > 3 and n % 3 == 0:
        continue
    
    elif n > 5 and n % 5 == 0:
         continue
    
    elif n > 7 and n % 7 == 0:
        continue
    
    else:
        print(f'{n}', end=' ')
    
    contar = contar + 1

print(f'\nO total de números primos é {contar}')
    
    