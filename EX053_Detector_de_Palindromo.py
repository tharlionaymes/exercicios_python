# EXERCÍCIO 053 - Detector de Palíndromo

frase = input('Digite uma frase: ').upper()

frase_invertida = frase[::-1].upper()

if frase.replace(" ","") == frase_invertida.replace(" ",""):
    print('A frase digitada é um PALÍNDROMO')
else:
    print('A frase digitada NÃO SÃO IGUAIS')

print(f'Frase Digitada >>> {frase}')
print(f'Frase Invertida >>> {frase_invertida}')
