# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_por_hora = float(input("Insira quanto você ganha por hora em R$: "))
horas_trabalhadas = int(input("Insira a quantidade de horas que você trabalha: "))
salario = valor_por_hora * horas_trabalhadas
print(f"Seu salário é de R${salario:.2f}")
