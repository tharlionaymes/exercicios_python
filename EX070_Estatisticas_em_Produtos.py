# EXERCÍCIO 070 - Estatísticas em Produtos

linha = '#' * 50
titulo = 'ESTATÍSTICAS EM PRODUTOS'

print(linha)
print(titulo.center(50))
print(linha)

continuar = 'S'
contador_compra = 0
contador_produto_maior1000 = 0
produto = 'produto'

lista_nome_produto = []
lista_preco_produto = []


while continuar == 'S':

    nome_produto = str(input('Nome do Produto: ')).strip().upper()
    lista_nome_produto.append(nome_produto)
    
    preco_produto = int(input('Preço do Produto: '))
    lista_preco_produto.append(preco_produto)
    

    if preco_produto > 1000:
        contador_produto_maior1000 += 1
    
       
    continuar = input('\nQUER CONTINUAR [S/N]? ').upper()
    
    
if contador_produto_maior1000 >= 2:
        produto = 'produtos'
       
produtos_mais_caros = int(sum(lista_preco_produto))

"""mais_barato = min(lista_preco_produto)
posicao_mais_barato = lista_preco_produto.index(mais_barato)
nome_mais_barato = lista_nome_produto[posicao_mais_barato]"""

nome_mais_barato = lista_nome_produto[lista_preco_produto.index(min(lista_preco_produto))]

print(f'\nO total gasto na compra = {produtos_mais_caros}'
      f'\nHá {contador_produto_maior1000} {produto} com valor superior a R$ 1000,00'
      f'\nO nome do produto mais barato é {nome_mais_barato}')
