# EXERCÍCIO 039 - Alistamento Militar

from datetime import date

ano = date.today()

ano_nascimento = int(input('Digite o seu ano de nascimento: '))

condicao = ano.year - ano_nascimento

diferenca = condicao - 18

if condicao == 18:
    print('Você deverá se alistar este ano.')

elif condicao <= 18:
    print(f'Ainda falta {abs(diferenca)} ano(s) para você se alistar')

elif condicao >= 18:
    print(f'Já passou {diferenca} ano(s) do tempo de seu alistamento.')
