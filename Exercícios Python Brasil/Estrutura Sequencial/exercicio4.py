# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = []
while len(notas) < 4:
    nota = float(input('Insira uma nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"A média dos bimestres é {media:.2f}")