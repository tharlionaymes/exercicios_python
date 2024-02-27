# EXERCÍCIO 019 - Sorteando um Item na Lista

from random import choice

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = choice(lista)

print('O aluno escolhido foi {}!'.format(sorteio))
