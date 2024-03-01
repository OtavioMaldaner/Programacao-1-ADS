# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Insira o valor do salário do funcioário em R$: "))
aumento = 0
aumento_percetual: ""

if salario <= 280:
    aumento = salario * 1.2
    aumento_percetual = "20%"
elif salario > 280 and salario <= 700:
    aumento = salario * 1.15
    aumento_percetual = "15%"
elif salario > 700 and salario <= 1500:
    aumento = salario * 1.1
    aumento_percetual = "10%"
else:
    aumento = salario * 1.05
    aumento_percetual = "5%"
aumento_total = aumento - salario
print(f"""
salário antigo: R${salario:.2f}
percentual de aumeto: {aumento_percetual}
valor do aumento: R${aumento_total:.2f}
novo salário: R${aumento:.2f}
""")