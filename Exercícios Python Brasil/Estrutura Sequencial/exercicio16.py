# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1
# litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.
tamanho = float(input("Digite o tamanho em m²: "))
lata = 18
preco = 80
litros_total = tamanho / 3
latas_total = 0
if litros_total % lata > 0:
    latas_total = (litros_total // lata) + 1
else:
    latas_total = litros_total / lata
preco_total = latas_total * preco
print(f"Você deve comprar {latas_total} latas de tinta, que custarão R${preco_total:.2f}")
