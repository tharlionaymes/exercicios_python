# EXERCÍCIO 011 - Pintando Parede

largura = float(input('Digite a largura da parede em metros: '))

altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

qtd_tinta = (area /2)

print(f'A largura da parede é {largura:.2f} m, a altura é {altura:.2f} m, a área dela é {area:.2f} m² e a quantidade de tinta necessária para pintar essa parede é {qtd_tinta:.0f} litros')
