# EXERCÍCIO 067 - Tabuada v3.0

num_1 = int(input("Qual tabuada você quer? "))
n = 0
escolha = 'S'
while escolha == 'S':
    for n in range(1, 11):
        multi = num_1 * n
        print(f'{num_1} * {n} = {multi}')
    print('-' * 15)
    escolha = input('Quer a tabuada de outro número [S/N]? ').upper()
    if escolha != 'S':
        continue
    num_1 = int(input("\nQual tabuada você quer? "))
else:
    print('ATÉ A PRÓXIMA!!!')
