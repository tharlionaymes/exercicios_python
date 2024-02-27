# EXERCÍCIO 058 - Jogo da Adivinhação v2.0

from random import randint

linha = '#' * 50
titulo = 'JOGO DA ADIVINHAÇÃO V1.0'

print(linha)
print(titulo.center(50))
print(linha)

contador = 0

while True:

    contador += 1

    computer = randint(1, 7)

    usuario = int(input('\nDe 1 a 7, qual foi o número escolhido pelo computador?: '))

    if computer == usuario:
        print('\nPARABÉNS, VOCÊ VENCEU!')
        print(f'\nVocê demorou {contador} rodadas para vencer.')
        break

    else:
        print(f'O número do computador é {computer}. VOCÊ PERDEU, ATÉ A PRÓXIMA!')
