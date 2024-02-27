# EXERCÍCIO 037 - Conversor de Bases Numéricas

numero_qualquer = int(input('Digite um número inteiro qualquer: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

escolha = int(input('\nSua opção: '))

if escolha == 1:
    print(f'O {numero_qualquer} convertido em BINÁRIO é {bin(numero_qualquer)[2:]}')

elif escolha == 2:
    print(f'O {numero_qualquer} convertido em OCTAL é {oct(numero_qualquer)[2:]}')

elif escolha ==3:
     print(f'O {numero_qualquer} convertido em HEXADECIMAL é {hex(numero_qualquer)[2:]}')
     
else:
    print('Escolha um número válido!')
    
