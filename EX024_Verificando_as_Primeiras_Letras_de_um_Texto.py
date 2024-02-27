# EXERCÍCIO 024 - Verificando as Primeiras Letras de um Texto

name_city = str(input('Digite um nome de uma cidade: '))

name_city_maiusc = name_city.upper()

if 'SANTO' in name_city_maiusc:
    print('Há o nome SANTO na cidade!!!')

else:
    print('Não há o nome SANTO na cidade')

print(f'A cidade é {name_city_maiusc}')
