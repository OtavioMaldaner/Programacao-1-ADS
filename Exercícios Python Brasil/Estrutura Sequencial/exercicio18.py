# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
# download do arquivo usando este link (em minutos).
arquivo = float(input("Insira o tamanho do arquivo em MB: "))
velocidade = float(input("Insira a velocidade da internet em Mbps: "))
tempo = arquivo / velocidade
print(f"O tempo necessário para baixar o arquivo é de {tempo:.2f} segundos")