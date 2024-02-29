# Exercício 13: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

gen = input("Digite M para Mulher e H para Homem: ")
if gen.lower() == "h" or gen.lower() == "m":
    altura = float(input("Digite a sua altura: "))
    peso_ideal = 0

    if gen.lower() == "m":
        peso_ideal = (62.1 * altura) - 44.7
    elif gen.lower() == "h":
        peso_ideal = (72.7 * altura) - 58

    print(f"Seu peso ideal é {peso_ideal:.2f} kg")
else:
    print("Insira um gênero válido!")
