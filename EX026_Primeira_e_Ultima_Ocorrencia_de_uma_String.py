# EXERCÍCIO 026 - Primeira e Última Ocorrência de uma String

frase = str(input('Digite uma frase: '))

frase_minusc = frase.lower()

print(f'A letra "a" aparece {frase_minusc.count("a")} vezes.')
print(f'A primeira vez que ela aparece é na posição {frase_minusc.find("a")}')
print(f'A última vez que ela aparece é na posição {frase_minusc.rfind("a")}')
print(frase.upper())
