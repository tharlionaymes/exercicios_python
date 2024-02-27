# EXERCÍCIO 068 - Jogo do Par ou Ímpar

from random import randrange

linha = '#' * 50
titulo = 'JOGO DO PAR OU IMPAR'

print(linha)
print(titulo.center(50))
print(linha)

continuar = 'S'
contador_pc = 0
contador_usuario = 0
contador_empate = 0

while continuar == 'S':
    
    escolha_usuario = input('\nESCOLHA PAR OU IMPAR [P/I]: ').upper()
    
    if escolha_usuario != 'P' and escolha_usuario != 'I':
        print('\nVOCÊ DIGITOU A OPÇÃO ERRADA!!')
      

    elif escolha_usuario == 'P':
        par_computador = randrange(0,11,2)
        par_usuario = int(input('\nDIGITE UM VALOR PAR DE 0 A 10: '))
        while par_usuario % 2 != 0:
            print('\nVALOR ERRADO...DIGITE UM VALOR PAR.')
            par_usuario = int(input('\nDIGITE UM VALOR PAR DE 0 A 10: '))
          
        if par_usuario > par_computador:
            print(f'\nVOCÊ GANHOU! VOCÊ JOGOU {par_usuario} E O COMPUTADOR JOGOU {par_computador}.')
            contador_usuario += 1
        
        elif par_usuario < par_computador:
            print(f'\nVOCÊ PERDEU! VOCÊ JOGOU {par_usuario} E O COMPUTADOR JOGOU {par_computador}.')
            contador_pc += 1
        
        else:
            print(f'\nEMPATE! VOCÊ JOGOU {par_usuario} E O COMPUTADOR JOGOU {par_computador}.')
            contador_empate += 1
    
    elif escolha_usuario == 'I':
        impar_computador = randrange(1,11,2)
        impar_usuario = int(input('\nDIGITE UM VALOR IMPAR DE 0 A 10: '))
        while impar_usuario % 2 == 0:
            print('\nVALOR ERRADO...DIGITE UM VALOR IMPAR.')
            impar_usuario = int(input('\nDIGITE UM VALOR IMPAR DE 0 A 10: '))
    
        if impar_usuario > impar_computador:
            print(f'\nVOCÊ GANHOU! VOCÊ JOGOU {impar_usuario} E O COMPUTADOR JOGOU {impar_computador}.')
            contador_usuario += 1
        
        elif impar_usuario < impar_computador:
            print(f'\nVOCÊ PERDEU! VOCÊ JOGOU {impar_usuario} E O COMPUTADOR JOGOU {impar_computador}.')
            contador_pc += 1
        
        else:
            print(f'\nEMPATE! VOCÊ JOGOU {impar_usuario} E O COMPUTADOR JOGOU {impar_computador}. ')
            contador_empate += 1
    
    continuar = input('\nQUER CONTINUAR [S/N]? ').upper()

print(f'\nTOTAL: \nVITÓRIA = {contador_usuario}, \nDERROTA = {contador_pc} \nEMPATE = {contador_empate}')

print('\nATÉ A PRÓXIMA!!!')       