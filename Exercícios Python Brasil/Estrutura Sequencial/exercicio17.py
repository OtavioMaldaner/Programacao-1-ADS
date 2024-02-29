import math
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
# cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
# em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
def calcular_latas(area):
    return math.ceil((area * 1.1) / 108)
def calcular_galoes(area):
    return math.ceil((area * 1.1) / 21.6)
def calcular_combinacao(area):
    latas = calcular_latas(area)
    galoes = calcular_galoes(area)
    preco_latas = latas * 80
    preco_galoes = galoes * 25
    latas_combinacao = math.floor(area / 108)
    area_restante = area % 108
    galoes_combinacao = math.ceil(area_restante / 21.6)
    preco_combinacao = (latas_combinacao * 80) + (galoes_combinacao * 25)

    return (latas, preco_latas), (galoes, preco_galoes), (latas_combinacao, galoes_combinacao, preco_combinacao)
def imprimir_resultados(latas_resultado, galoes_resultado, combinacao_resultado):
    print("Situação 1: Comprar apenas latas de 18 litros")
    print(f"Quantidade de latas: {latas_resultado[0]}")
    print(f"Preço total: R$ {latas_resultado[1]:.2f}\n")

    print("Situação 2: Comprar apenas galões de 3,6 litros")
    print(f"Quantidade de galões: {galoes_resultado[0]}")
    print(f"Preço total: R$ {galoes_resultado[1]:.2f}\n")

    print("Situação 3: Misturar latas e galões")
    print(f"Quantidade de latas: {combinacao_resultado[0]}")
    print(f"Quantidade de galões: {combinacao_resultado[1]}")
    print(f"Preço total: R$ {combinacao_resultado[2]:.2f}")

def main():
    area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
    latas_resultado, galoes_resultado, combinacao_resultado = calcular_combinacao(area)
    imprimir_resultados(latas_resultado, galoes_resultado, combinacao_resultado)

if __name__ == "__main__":
    main()