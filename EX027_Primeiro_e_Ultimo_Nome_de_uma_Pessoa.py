# EXERCÍCIO 027 - Primeiro e Último Nome de uma Pessoa 

nome = input('Digite seu nome completo: ').upper()

frase = nome.split()

print(f'\nSeu primeiro nome é {frase[0]}')
print(f'\nSeu último nome é {frase[-1]}')
