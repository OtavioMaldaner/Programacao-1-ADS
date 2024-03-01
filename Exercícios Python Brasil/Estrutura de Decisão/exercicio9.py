# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))
lista = [num1, num2, num3]
reversa = sorted(lista, reverse=True)
print(reversa)