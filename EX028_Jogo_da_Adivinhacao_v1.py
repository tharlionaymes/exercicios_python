# EXERCÍCIO 028 - Jogo da Adivinhação v1.0

from random import randint

linha = '#' * 50
titulo = 'JOGO DA ADIVINHAÇÃO V1.0'

print(linha)
print(titulo.center(50))
print(linha)

computer = randint(0,5)

usuario = int(input('\nDe 0 a 5, qual foi o número escolhido pelo computador?: '))

if computer == usuario:
    print('PARABÉNS, VOCÊ VENCEU!')

else:
    print(f'O número do computador é {computer}. VOCÊ PERDEU, ATÉ A PRÓXIMA!')
    