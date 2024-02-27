# EXERCÍCIO 055 — Maior e Menor da Sequência

lista = []

for peso in range(1, 6):
    seu_peso = int(input(f'Qual o peso da {peso}ª pessoa? '))
    lista.append(seu_peso)

print(f'\nOs pesos digitados são {lista}')
print(f'\nO menor peso lido foi {min(lista)}.')
print(f'\nO maior peso lido foi {max(lista)}.')
