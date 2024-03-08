# Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.
ano = input("Insira um ao para ver se é bissexto: ")
if int(ano) % 4 == 0 and not ano.endswith("00"):
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")