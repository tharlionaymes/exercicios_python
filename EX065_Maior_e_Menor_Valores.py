# EXERCÍCIO 065 - Maior e Menor Valores


linha = '#' * 50
titulo = 'VAI DIGITANDO AÊ.'

print(linha)
print(titulo.center(50))
print(linha)

lista = []

while True:
    num_digitado = int(input('Digite um número: '))
    lista.append(num_digitado)
    continuar = input('Quer digitar mais números [S/N]? ').upper()
    if continuar == 'N':
        break

print(f'A média entre todos os valores é {sum(lista) / len(lista):.2f}, '
      f'o maior valor é {max(lista)} e o menor valor é {min(lista)}.')
