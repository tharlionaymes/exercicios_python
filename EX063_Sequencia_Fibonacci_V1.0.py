# EXERCÍCIO 063 - Sequência de Fibonacci V1.0

linha = '#' * 50
titulo = 'SEQUÊNCIA DE FIBONACCI V1.0'

print(linha)
print(titulo.center(50))
print(linha)

n_esimo = int(input('\nQuantos termos vocês quer? '))

ultimo_termo = 1                       # Variavel para fazer a sequencia

penultimo_termo = 0                    # Variavel para fazer a sequencia

n = 2                                  # Variavel para validacao do while

# listas = []

entre_num = ''                          # Variavel usada para formatar algo entre os números

if n_esimo <= 2:                        # Se o numero digitado for menor que 2 ativa o if
    for i in range(n_esimo):            # O range sera o numero digitado
        print(f'{1}', end='')

elif n_esimo >= 2:                      # Se o numero digitado for maior que 2 ativa o elif

    print(f'{ultimo_termo}', end=',')   # mostra o numero 1 antes de entrar no while

    while n <= n_esimo:                 # Valida o while com o n menor ou igual ao valor digitado
        termo_atual = ultimo_termo + penultimo_termo      # formula do fibonacci
        penultimo_termo = ultimo_termo                    # Isso é importante para manter a sequencia
        ultimo_termo = termo_atual                        # Isso é importante para manter a sequencia
        n += 1                                            # Acrescenta mais 1 ao n para rodar mais uma vez o while
        print(entre_num, end=' ')         # usado aqui para acrescentar um espaço entre os números
        print(f'{termo_atual}', end='')   # esse end='' nao pode ser retirado se quiser os numeros na horizontal
        entre_num = ','                   # usado aqui para acrescentar uma virgula entre os números
    """    listas.append(termo_atual)     # iria adicionar em uma lista
    print()                               # print qualquer para pular linhas rsrs
    print(* listas, sep=', ')             # esse comando do * remove os colchetes das listas
"""
