from collections import Counter
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
lado1 = float(input('Digite o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

lados = [lado1, lado2, lado3]
contador = Counter(lados)
repetidos = {chave: valor for chave, valor in contador.items() if valor > 1}

for item, contagem in repetidos.items():
    if contagem == 3:
        print("O triângulo é equilátero")
    elif contagem == 2:
        print("O triangulo é isóceles")
    else:
        print("O triangulo é escaleno")