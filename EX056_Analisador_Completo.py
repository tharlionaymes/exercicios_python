# # EXERCÍCIO 056 — Analisador Completo

# Todas as listas usadas separadas por finalidade
lista_nome = []
lista_idade = []
lista_sexo = []
lista_nome_homem = []
lista_idade_homem = []
lista_idade_mulher = []

# O loop FOR vai rodar do 1 ao 4 capturando o nome, idade e sexo das pessoas e adicionando-os as listas respectivas
for c in range(1, 5):
    print(f'-------------- {c}ª pessoa ----------------')
    nome = str(input('NOME: ')).strip().upper()           # Captura o nome, retira os espaços e o coloca em maiusculo
    lista_nome.append(nome)                               # Adiciona na lista_nome

    idade = int(input('IDADE: '))                         # Captura a idade
    lista_idade.append(idade)                             # Adiciona na lista_idade

    sexo = str(input('SEXO [M/F]: ')).strip().upper()     # Captura o sexo, retira os espaços e o coloca em maiusculo
    lista_sexo.append(sexo)                               # Adiciona na lista_sexo

    if sexo == 'M':                                       # Condicao para saber se é do sexo masculino
        lista_nome_homem.append(nome)                     # A nova informacao é adicionada em uma nova lista
        lista_idade_homem.append(idade)                   # A nova informacao é adicionada em uma nova lista
    
    if sexo == 'F' and idade < 20:                        # Condicao para saber se é do sexo fem e tem menos de 20 anos
        lista_idade_mulher.append(idade)                  # A nova informacao é adicionada em uma nova lista

media_idade = int(sum(lista_idade) / len(lista_idade))    # Calcular a media de idade do grupo

mais_idoso = max(lista_idade_homem)                       # Descobre quem é o mais idoso
posicao_mais_idoso = lista_idade_homem.index(mais_idoso)  # Descobre a posicao do mais idoso
nome_mais_idoso = lista_nome_homem[posicao_mais_idoso]    # Descobre o nome do mais idoso

# Exibe na tela os resultados
print(f'A média de idade do grupo é {media_idade}')
print(f'O homem mais velho é {nome_mais_idoso}')
print(f'O total de mulheres que tem idade abaixo de 20 anos é/são {len(lista_idade_mulher)}')
