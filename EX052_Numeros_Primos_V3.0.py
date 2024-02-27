# EX052 - Numeros Primos v3.0

lista = list()
tamanho = 0
contar = 0
y = 1
x = int(input('Digite um número inteiro: '))

if x:
    while y <= x:

        if x % y == 0:
            divisao = x / y
            lista.append(divisao)
            tamanho = len(lista)
        y = y + 1

    if tamanho >= 3 or x <= 1 or x > 2 and x % 2 == 0 or x > 3 and x % 3 == 0 or x > 5 and x % 5 == 0 or x > 7 \
            and x % 7 == 0:
        print('NAO PRIMO')

    else:
        print('PRIMO')
