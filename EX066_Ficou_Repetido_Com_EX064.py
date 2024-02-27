# EXERCÍCIO 064 - Tratando Vários Valores v1.0

linha = '#' * 50
titulo = 'VAI DIGITANDO UM NÚMERO. DIGITE 999 E PARE.'

print(linha)
print(titulo.center(50))
print(linha)

conta_digitado = 0
lista = []

while True:
    num_digitado = int(input('Digite um número: '))
    if num_digitado == 999:
        break
    lista.append(num_digitado)
    conta_digitado += 1

print(f'Foram digitados {conta_digitado} números e a soma entre eles foi {sum(lista)}')
