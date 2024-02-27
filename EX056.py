"""EXERCÍCIO 056 — Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
from collections import defaultdict

lista_nome = ['jose','maria','carlos']
lista_idade = [40,50,60]
lista_sexo = ['m','f','m']
nome = 0
idade = 0
sexo = 0

# O loop FOR vai rodar do 1 ao 4 capturando o nome, idade e peso das pessoas e adicionando-os as listas respectivas
"""for x in range(1, 4):
    nome = str(input(f'Digite o nome da {x}ª pessoa: '))
    idade = int(input(f'Digite a idade da {x}ª pessoa: '))
    sexo = str(input(f'Digite o sexo [M/F] da {x}ª pessoa: '))
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)"""

"""Para descobrir a média de idade do grupo.
Tive que calcular a madia_idade usando funções de listas("sum" -> soma e "len" -> tamanho)"""

"""media_idade = int(sum(lista_idade) / len(lista_idade))  # Calcular a media de idade
print(media_idade)"""

"""Para descobrir qual é o nome do homem mais velho.
Fazer um "se" na lista de sexo e descobrir se tem o "m"
Tive que descobrir quem é o mais idoso e a posicao que ele ocupa na lista"""


posicao = defaultdict(list); # Define o objeto que armazenará os índices de cada elemento

for indice, sexo in enumerate(lista_sexo): # Percorre todos os elementos da lista

    posicao[sexo].append(indice) # Adiciona o índice do valor na lista de índices

print(posicao[sexo]) # Exibe o resultado
    
    
"""if 'm' in lista_sexo:
    posicao_m = lista_sexo.index('m')  # Descobre a posicao dos masculinos
    print(posicao_m)
else:
    print('Não há integrantes do sexo Masculino.')"""
    
""" mais_idoso = max(lista_idade)  # Descobre quem é o mais idoso
posicao_mais_idoso = lista_idade.index(mais_idoso)  # Descobre a posicao do mais idoso
print(lista_nome[posicao_mais_idoso])"""

"""
Para descobrir quantas mulheres têm menos de 20 anos. 
"""