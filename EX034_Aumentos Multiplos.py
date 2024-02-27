# EXERCÍCIO 034 -  Aumentos Múltiplos

digite_seu_salario = float(input('Digite o seu salário R$:'))

salario_funcionario = int(digite_seu_salario)

if salario_funcionario <= int(1250):
    salario_aumento10 = salario_funcionario * 1.1
    print(f'O seu salário sofreu um aumento de 10%. Seu valor agora é {salario_aumento10:.2f}')

else:
    salario_aumento15 = salario_funcionario * 1.15
    print(f'O seu salário sofreu um aumento de 15%. Seu valor agora é {salario_aumento15:.2f}')
