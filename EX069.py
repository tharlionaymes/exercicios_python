# EXERCÍCIO 069 - Análise de Dados do Grupo

linha = '#' * 50
titulo = 'ANÁLISE DE DADOS DO GRUPO'

print(linha)
print(titulo.center(50))
print(linha)

continuar = 'S'
contador_maior18 = 0
contador_homens = 0
contador_mulhermenor20 = 0
pessoa = 'pessoa'
homem = 'HOMEM'
mulher = 'MULHER'
cadastrado = 'cadastrados'

while continuar == 'S':

    idade = int(input('IDADE: '))     

    sexo = str(input('SEXO [M/F]: ')).strip().upper()                               

    if idade > 18:
        contador_maior18 += 1
        
    
    if sexo == 'M':                                                                 
        contador_homens += 1
        
    
    if sexo == 'F' and idade < 20:                      
        contador_mulhermenor20 += 1
        
    
    continuar = input('\nQUER CONTINUAR [S/N]? ').upper()
    
    
if contador_maior18 >= 2:
        pessoa = 'pessoas'
        
if contador_homens >= 2:
        homem = 'HOMENS'
        cadastrado = 'cadastrados'

if contador_mulhermenor20 >= 2:
        mulher = 'MULHERES'

print(f'\nHá {contador_maior18} {pessoa} com mais de 18 anos '
      f'\nHá {contador_homens} {homem} {cadastrado}'
      f'\nHá {contador_mulhermenor20} {mulher} com menos de 20 anos')
  