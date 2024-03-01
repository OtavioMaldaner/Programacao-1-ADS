# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
# o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
valor_hora = float(input("Digite o seu salário por hora em R$: "))
horas = float(input("Digite a quatidade de horas que trabalha no mês: "))
salario = valor_hora * horas
salario_bruto = salario
desconto_ir = ""
fgts = salario_bruto * .11
if salario_bruto <= 900:
    pass
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = "5%"
    salario_bruto *= 0.95
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = "10%"
    salario_bruto *= .9
else:
    desconto_ir = "20%"
    salario_bruto *= .8
salario_ir = salario_bruto
salario_bruto *= .9 # Desconto INSS
salario_bruto *= .97 # Desconto Sidicato
descontos = salario - salario_bruto
print(f"""
Salário Bruto: ({valor_hora} * {horas})        : R$ {salario}
(-) IR ({desconto_ir})                     : R$   {salario - salario_ir}
(-) INSS (10%)                 : R$  {salario * .1}
FGTS (11%)                      : R$  {fgts}
Total de descontos              : R$  {descontos:.2f}
Salário Liquido                 : R$  {salario_bruto:.2f}
""")