# EXERCÍCIO 041 — Classificando Atletas

from datetime import date

ano_atual = date.today()

ano_nascimento = int(input('Digite o ano do seu nascimento: '))

condicao = ano_atual.year - ano_nascimento

if condicao <= 9:
    print(f'Você e MIRIM, pois tem {condicao} anos')

elif 9 < condicao <= 14:
    print(f'Você e INFANTIL, pois tem {condicao} anos')

elif 14 < condicao <= 19:
    print(f'Você e JUNIOR, pois tem {condicao} anos')

elif 19 < condicao <= 25:
    print(f'Você e SENIOR, pois tem {condicao} anos')

else:
    print(f'Você e MASTER, pois tem {condicao} anos')
