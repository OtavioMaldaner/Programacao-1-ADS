# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Insira o lado do quadrado em centímetros: "))
area = lado * lado
perimetro = 2 * lado
print(f"A área do quadrado é {area:.2f} cm² e o perímetro é {perimetro:.2f} cm²")