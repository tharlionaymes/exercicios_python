# EXERCÍCIO 048 - Soma Ímpares Múltiplos de Três

soma = 0
contar = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        contar = contar + 1

print(f'A soma de todos os {contar} valores solicitados é {soma}')
