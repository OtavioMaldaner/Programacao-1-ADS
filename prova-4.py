quadrado = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
soma_linhas = []
soma_colunas = []
soma_vapo = []
for linha in quadrado:
    soma_linhas.append(sum(linha))
    for index, coluna in enumerate(linha):
        soma_colunas.append(linha[index])
diagonal_principal = quadrado[0][0] + quadrado[1][1] + quadrado[2][2]
diagonal_secundaria = quadrado[0][2] + quadrado[1][1] + quadrado[2][0]
soma_vapo = [diagonal_principal, diagonal_secundaria]
if sum(soma_linhas) == sum(soma_colunas):
    if sum(soma_linhas) == sum(soma_vapo):
        print('É um quadrado mágico!')
    else:
        print('Não é um quadrado mágico')
else:
    print('Não é um quadrado mágico')