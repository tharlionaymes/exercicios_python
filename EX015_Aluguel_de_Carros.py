# EXERCÍCIO 015 - Aluguel de Carros

km_percorrido = float(input('Quantos KM foi percorrido? '))

dias_usado = int(input('Quantos dias o carro foi usado? '))

preco_total_dias = int(60 * dias_usado)

preco_total_km = float(0.15 * km_percorrido)

#preco_total = (60 * dias_usado) + (0.15 * km_percorrido)

preco_total = preco_total_dias + preco_total_km

#print(f'Foi percorrido {km_percorrido} KM, o valor total pelo KM é R$ {preco_total_km:.2f}\nO carro foi usado por {dias_usado} dias, o valor total pelos dias é R$ {preco_total_dias:.2f}\nO total a ser pago pela locação é R$ {preco_total:.2f}.')

print(f'Foi percorrido {km_percorrido} KM, o valor total pelo KM é R$ {preco_total_km:.2f}'
f'\nO carro foi usado por {dias_usado} dias, o valor total pelos dias é R$ {preco_total_dias:.2f}'
f'\nO total a ser pago pela locação é R$ {preco_total:.2f}.')


