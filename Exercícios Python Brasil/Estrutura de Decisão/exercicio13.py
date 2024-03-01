# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_da_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

numero = int(input('Digite um número inteiro: '))
dia_da_semana = dias_da_semana.get(numero)

if dia_da_semana:
    print(f"É {dia_da_semana}!")
else:
    print("Esse número não corresponde a um dia da semana")
