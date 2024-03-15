dias = int(input('Dias de locação: '))
km = int(input('Quilometragem percorrida: '))
valor = (dias * 90) + ((km % 100) * 12)
print(f'O valor total da locação é de R${valor:.2f}')