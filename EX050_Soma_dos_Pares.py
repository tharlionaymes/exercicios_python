# EXERCÍCIO 050 - Soma dos Pares

num_digitado = 0

soma = 0

for num_digitado in range (0, 6):
    num_digitado = int(input('Digite um número: '))
    if num_digitado % 2 == 0:
        soma = soma + num_digitado
print(f'\nA soma dos números pares é {soma}')
