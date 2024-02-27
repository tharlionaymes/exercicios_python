# EXERCÍCIO 017: Catetos e Hipotenusa

cateto_oposto = float(input('Qual o cateto oposto? '))

cateto_adjacente = float(input('Qual o cateto adjacente'))

hipotenusa = float((cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5)

print(f'A hipotenusa do triângulo retângulo é {hipotenusa:.2f}')
