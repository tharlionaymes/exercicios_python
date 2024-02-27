# EX052 - Numeros Primos v2.0

lista = list()
tamanho = 0
contar = 0

for x in range(2, 1000):
    y = 1
    lista.clear()

    while y <= x:

        if x % y == 0:
            divisao = x / y
            lista.append(divisao)
            tamanho = len(lista)
        y = y + 1

        if tamanho == 3:
            break

        if x > 2 and x % 2 == 0:
            break

        elif x > 3 and x % 3 == 0:
            break

        elif x > 5 and x % 5 == 0:
            break

        elif x > 7 and x % 7 == 0:
            break

    else:
        print(x, end=' ')
        contar = contar + 1

    x = x + 1

print(f'\nO total de números primos é {contar}')
