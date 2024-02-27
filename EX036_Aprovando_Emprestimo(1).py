# EXERCÍCIO 036 - Aprovando Empréstimo

valor_casa = int(input('Digite o valor da casa R$: '))

salario_comprador = int(input('Digite o valor do seu salário R$: '))

tempo_parcelas = int(input('Digite quantos anos você quer pagar o financiamento: '))

meses = tempo_parcelas * 12

prestacao_mensal = valor_casa / meses

if prestacao_mensal >= (salario_comprador * 0.3):
    print(' O empréstimo foi NEGADO!')
    print(f'O valor da parcela será R$ {prestacao_mensal:.2f} por mês e excede 30% (R$ {salario_comprador * 0.3:.2f}) do seu salário.')

else:
    print('PARABÉNS! Empréstimo APROVADO!')
    print(f'O valor da parcela será R$ {prestacao_mensal:.2f} por mês.')
