# EXERCÍCIO 029 - Radar Eletrônico

velocidade_carro = float(input('Digite a velocidade do carro: '))

if velocidade_carro > int(80):
    print(f'Você Ultrapassou o Limite Permitido da Via. Será MULTADO em R$ {(velocidade_carro - 80) * 7 :.2f}.')
    
else:
    print('DENTRO DO LIMITE! Boa Viagem.')
