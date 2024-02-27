# EXERCÍCIO 060 — Cálculo do Fatorial

num = int(input('Digite um Número: '))  # Pede para o usuário digitar um número e o aloca na variável 'num'

fatorial = 1    # Variável com o nome de 'fatorial' com valor igual a 1 para ter como fazer a multiplicação

print(f'{num}! = ', end=' ')  # Mostra na tela o valor da variável 'num' com sinal de '!' e o sinal de '='
                              # O comando end=' ' desse jeito deixa um espaço em branco no final do resultado mostrado

while num >= 1:                # Enquanto 'num' for maior ou igual a 1 o laço não termina.

    print(num, end=' ')        # Mostra na tela o 'num'
    if num > 1:                # Se esse 'num' for maior que 1
        print('X', end=' ')    # Irá mostrar um X
    else:                      # Se não
        print(end=' = ')       # Irá mostrar um sinal de igual no final do resultado

    fatorial = fatorial * num  # Pega a variável 'fatorial' e multiplica ela com o 'num'
    num = num - 1              # Pega o valor de 'num' e diminui por 1
    if num == 0:               # Se 'num' for igual a 0 o laço é finalizado
        break                  # Encerra o programa se ele for igual a 0
print(fatorial)                # Ao final do laço é mostrado na tela o resultado do fatorial
