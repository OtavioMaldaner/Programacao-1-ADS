distancia = int(input('Insira a distância da cidade de Ambrósia: '))
reais = float(input('Insira o dinheiro de Ambrósio em R$: '))
litros = float(input('Insira a capacidade de do tanque do seu carro em L: '))
postos = int(input('Insira a quantidade de postos de combustível disponíveis: '))
gasolina = float(input('Insira a o preço da gasolina em R$: '))
media = 10
km_disponivel = litros * media
litros_necessarios = distancia / media
distancia_postos = distancia / postos
tanques = litros / litros_necessarios
comprar_litros = litros_necessarios - litros
compra = comprar_litros * gasolina
if tanques > 1:
    if compra > reais:
        print('Não pode viajar')
    else:
        if tanques <= postos:
            print('Não pode viajar')
        else:
            print(f'Pode viajar e sobram R${reais - compra:.2f}')
else:
    if reais - compra < 0:
        print('Não pode viajar!')
    else:
        print(f'Pode viajar e sobram R${reais - compra:.2f}')