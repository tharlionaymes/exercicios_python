# EXERCÍCIO 051 - Progressão Aritmética

termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))

for n in range (1, 11):
    
    termo_geral = termo + (n - 1) * razao
    
    print(f'a{n} = {termo_geral}')
    