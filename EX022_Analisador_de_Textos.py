# EXERCÍCIO 022 - Analisador de Textos

nome = str(input('Digite algo: '))
frase = nome.split()

print(f'\nTodas as letras maiúsculas: {nome.upper()}\n')
print(f'Todas as letras minúsculas: {nome.lower()}\n')
print(f'Quantidade de letras ao todo (sem considerar espaços): {len(nome.replace(" ",""))}\n')
print(f'A primeira palavra é: {frase[0]}\n')
print(frase)
