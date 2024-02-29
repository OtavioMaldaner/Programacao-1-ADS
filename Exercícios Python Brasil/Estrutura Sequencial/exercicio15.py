# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
hora = float(input("Digite o salário por hora em R$: "))
horas_trabalhadas = int(input("Insira a quatidade de horas que trabalhou no mês: "))
salario = hora * horas_trabalhadas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - ir - inss - sindicato
print(f"Você pagará R${ir:.2f} de imposto de reda")
print(f"Você pagará R${inss:.2f} de INSS")
print(f"Você pagará R${sindicato:.2f} de sindicato")
print(f"Você receberá R${salario_liquido:.2f} de salário líquido")

