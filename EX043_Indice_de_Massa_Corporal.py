# EXERCÍCIO 043 — Índice de Massa Corporal

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(F'Seu imc é {imc:.2f} e você está ABAIXO DO PESO')

elif 18.5 <= imc <= 25:
    print(F'Seu imc é {imc:.2f} e você está com PESO IDEAL')

elif 25 <= imc <= 30:
    print(F'Seu imc é {imc:.2f} e você está com SOBREPESO')

elif 30 <= imc <= 40:
    print(F'Seu imc é {imc:.2f} e você está com OBESIDADE')

else:
    print(F'Seu imc é {imc:.2f} e você está com OBESIDADE MÓRBIDA')
