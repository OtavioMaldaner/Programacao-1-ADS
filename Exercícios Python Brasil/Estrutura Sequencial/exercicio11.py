# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))
# a:
print("a: ", (primeiro * primeiro) / (segundo / 2))

# b:
print("b: ", ((3 * primeiro) + terceiro))

# c:
print("c: ", terceiro ** 3)