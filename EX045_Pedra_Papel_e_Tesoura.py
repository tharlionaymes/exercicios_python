# EXERCÍCIO 045 - Pedra, Papel e Tesoura

import random

escolha_pc = random.choice(['PAPEL', 'PEDRA', 'TESOURA'])

print('ESCOLHA UMA OPÇÃO'
      '\n[1] PAPEL'
      '\n[2] PEDRA'
      '\n[3] TESOURA')

escola_usuario = int(input('\nQual a opção? '))

if escola_usuario == 1 and escolha_pc == 'PAPEL':
    print(f'EMPATOU, o usuário jogou PAPEL e o computador jogou {escolha_pc}')

elif escola_usuario == 1 and escolha_pc == 'PEDRA':
    print(f'VOCÊ GANHOU, o usuário jogou PAPEL e o computador jogou {escolha_pc}')

elif escola_usuario == 1 and escolha_pc == 'TESOURA':
    print(f'VOCÊ PERDEU, o usuário jogou PAPEL e o computador jogou {escolha_pc}')

elif escola_usuario == 2 and escolha_pc == 'PAPEL':
    print(f'VOCÊ PERDEU, o usuário jogou PEDRA e o computador jogou {escolha_pc}')

elif escola_usuario == 2 and escolha_pc == 'PEDRA':
    print(f'EMPATOU, o usuário jogou PEDRA e o computador jogou {escolha_pc}')

elif escola_usuario == 2 and escolha_pc == 'TESOURA':
    print(f'VOCÊ GANHOU, o usuário jogou PEDRA e o computador jogou {escolha_pc}')

elif escola_usuario == 3 and escolha_pc == 'PAPEL':
    print(f'VOCÊ GANHOU, o usuário jogou TESOURA e o computador jogou {escolha_pc}')

elif escola_usuario == 3 and escolha_pc == 'PEDRA':
    print(f'VOCÊ PERDEU, o usuário jogou TESOURA e o computador jogou {escolha_pc}')

elif escola_usuario == 3 and escolha_pc == 'TESOURA':
    print(f'EMPATOU, o usuário jogou TESOURA e o computador jogou {escolha_pc}')
