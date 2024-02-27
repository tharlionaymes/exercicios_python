# EXERCÍCIO 031 - Custo da Viagem

distancia_viagem = float(input('Digite a distância da viagem em KM: '))

viagem_curta = (distancia_viagem) * 0.5
viagem_longa = (distancia_viagem) * 0.45

if distancia_viagem > 200:
    print(f'O valor da passagem será R$ {viagem_longa:.2f} ')
    
else:
    print(f'O valor da passagem será R$ {viagem_curta:.2f}')
