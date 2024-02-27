# EXERCÍCIO 054 - Grupo de Maioridade

from datetime import date

ano_atual = date.today()

cont_maiores = 0
cont_menores = 0

for nasc in range(0, 4):
    nasc = int(input('Digite uma data de nascimento: '))
    
    condicao = ano_atual.year - nasc
    
    diferenca = condicao - 18

    if condicao == 18 or condicao >= 18:
        cont_maiores += 1
    
    elif condicao <= 18:
        cont_menores += 1

print(f'{cont_maiores} MAIOR(ES) de IDADE.')    

print(f'{cont_menores} MENOR(ES) de IDADE.')    
