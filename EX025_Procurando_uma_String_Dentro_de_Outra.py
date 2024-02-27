# EXERCÍCIO 025 -  Procurando uma String Dentro de Outra

name_pessoa = str(input('Digite um nome: '))

name_pessoa_maiusc = name_pessoa.upper()

if 'SILVA' in name_pessoa_maiusc:
    print('Há SILVA no nome!!!')

else:
    print('Não há SILVA no nome')

print(f'O nome digitado é {name_pessoa_maiusc}')
