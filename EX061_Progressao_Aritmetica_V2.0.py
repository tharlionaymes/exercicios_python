# EXERCÍCIO 061 - Progressão Aritmética V2.0

termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))

n = 0
termo_geral = 0

while n <= 9:
    n += 1
    termo_geral = termo + (n - 1) * razao

    print(f'a{n} = {termo_geral}')
