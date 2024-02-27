# EXERCÍCIO 062 — Super Progressão Aritmética V3.0

termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))

n = 0
termo_geral = 0

while n <= 9:
    n += 1
    termo_geral = termo + (n - 1) * razao
    print(f'a{n} = {termo_geral}')

mais_termos = input('Quer mostrar mais termo [S/N]? ').upper()

while mais_termos == 'S':
    qtd_termos = int(input('Quantos termos a mais? '))
    for i in range(qtd_termos):
        n += 1
        termo_geral = termo + (n - 1) * razao
        print(f'a{n} = {termo_geral}')
        qtd_termos += 1
    mais_termos = input('Quer mostrar mais termo [S/N]? ').upper()

else:
    print('\nATÉ A PRÓXIMA!!!')
