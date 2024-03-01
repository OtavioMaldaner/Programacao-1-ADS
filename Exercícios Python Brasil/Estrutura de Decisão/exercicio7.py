# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f"O maior número é {maior} e o menor é {menor}")