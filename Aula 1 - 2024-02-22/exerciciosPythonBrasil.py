import math
# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Alo mundo")

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# numero = int(input("Insira um número: "))
# print(f"O número informado foi: {numero}")

# 3. Faça um Programa que peça dois números e imprima a soma.
# numero1 = int(input("Insira um número: "))
# numero2 = int(input("Insira outro número: "))
# soma = numero1 + numero2
# print(soma)

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# notas = []
# while len(notas) < 4:
#     nota = float(input('Insira uma nota: '))
#     notas.append(nota)
# media = sum(notas) / len(notas)
# print(f"A média dos bimestres é {media:.2f}")

# 5. Faça um Programa que converta metros para centímetros.
# metros = float(input('Digite o valor em metros: '))
# centimetros = int(metros * 100)
# print(f"O valor em centimetros é {centimetros} cm")

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# raio = float(input('Insira o raio de um círculo em cetímetros: '))
# area = 2 * math.pi * raio
# print(f"A área do círculo é {area:.2f} cm²")

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# lado = float(input("Insira o lado do quadrado em centímetros: "))
# area = lado * lado
# perimetro = 2 * lado
# print(f"A área do quadrado é {area:.2f} cm² e o perímetro é {perimetro:.2f} cm²")

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# valor_por_hora = float(input("Insira quanto você ganha por hora em R$: "))
# horas_trabalhadas = int(input("Insira a quantidade de horas que você trabalha: "))
# salario = valor_por_hora * horas_trabalhadas
# print(f"Seu salário é de R${salario:.2f}")

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
# fahrenheit = float(input("Insira uma temperatura em F: "))
# temperatura_celsius = 5 * ((fahrenheit - 32) / 9)
# print(f"A temperatura em Graus Célsius é {temperatura_celsius}ºC")

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input('Insira uma temperatura em graus célsius: '))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é {fahrenheit}F")
