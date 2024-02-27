# EXERCÍCIO 059 — Criando um Menu de Opções

num1 = int(input('DIGITE UM VALOR: '))
num2 = int(input('DIGITE UM VALOR: '))

while True:

    print('\n---------- MENU ----------')
    print('[1] SOMAR' '\n[2] MULTIPLICAR' '\n[3] MAIOR' '\n[4] NOVOS NÚMEROS' '\n[5] SAIR DO PROGRAMA')
    print('--------------------------')

    opcao = int(input('\nQUAL OPÇÃO? '))

    if opcao == 1:
        print(f'A soma é {num1 + num2}.')

    elif opcao == 2:
        print(f'A multiplicação é {num1 * num2}.')

    elif opcao == 3:
        opcao = [num1, num2]
        print(f'O maior número é {max(opcao)}')

    elif opcao == 4:
        print('\nESCOLHA OS NOVOS NÚMEROS')
        num1 = int(input('\nDIGITE UM VALOR: '))
        num2 = int(input('DIGITE UM VALOR: '))

    elif opcao == 5:
        break

print('\nATÉ A PRÓXIMA!!!')
