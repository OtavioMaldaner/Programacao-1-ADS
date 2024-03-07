# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
# sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

while True:
    print("Calculadora de raízes de equação de segundo grau")
    a = float(input("Insira o valor de A: "))
    if a == 0:
        print("O valor de A deve ser um numero diferente de 0")
        break
    b = float(input("Insira o valor de B: "))
    c = float(input("Insira o valor de C: "))
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print("O delta é negativo!")
        break
    elif delta == 0:
        x = (-b + math.sqrt(delta))/(2*a)
        print(f"O valor da raiz é {x:.2f}")
        break
    else:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print(f"Os valores das raízes são: {x1:.2f} e {x2:.2f}")
        break

