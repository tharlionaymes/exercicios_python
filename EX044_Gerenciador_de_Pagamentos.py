# EXERCÍCIO 044 - Gerenciador de Pagamentos

valor_da_compra = float(input('Digite o valor do produto: '))

print('FORMAS DE PAGAMENTO'
      '\n[1] 10% de desconto à vista no dinheiro/ cheque'
      '\n[2] 5% de desconto à vista no débito'
      '\n[3] em até 2x no crédito sem juros'
      '\n[4] em até 3x ou mais no cartão com juros de 20%')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    print(f'Sua compra de R$ {valor_da_compra:.2f} vai custar {valor_da_compra * 0.9:.2f} no final.')

elif opcao == 2:
    print(f'Sua compra de R$ {valor_da_compra:.2f} vai custar {valor_da_compra * 0.95:.2f} no final.')

elif opcao == 3:
    vezes1 = int(input('\nEm quantas vezes você quer fazer? '))
    print(f'Sua compra de R$ {valor_da_compra:.2f} vai ser parcelada em {vezes1} veze(s) de '
          f'{valor_da_compra / vezes1:.2f} com total de {valor_da_compra:.2f}')

elif opcao == 4:
    vezes2 = int(input('\nEm quantas vezes você quer fazer (3 ou mais? '))
    print(f'Sua compra de R$ {valor_da_compra:.2f} vai ser parcelada em {vezes2} vezes de '
          f'{valor_da_compra / vezes2:.2f} com total de {valor_da_compra * 1.2:.2f}')
