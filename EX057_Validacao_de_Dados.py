# EXERCÍCIO 057 - Validação de Dados

sexo = str(input('Qual o seu sexo [M/F]: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper()
    
print(f'Sexo {sexo} registrado com sucesso!')
