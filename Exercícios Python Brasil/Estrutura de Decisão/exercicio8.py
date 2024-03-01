# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input('Digite o preço de um produto: '))
produto2 = float(input('Digite o valor de outro produto: '))
produto3 = float(input('Digite o valor de mais um produto: '))
valores = [produto1, produto2, produto3]
menor = min(produto1, produto2, produto3)
for contador, produto in enumerate(valores):
    if produto == menor:
        print(f"O menor preço é R${produto:.2f}, do {contador + 1}º produto")