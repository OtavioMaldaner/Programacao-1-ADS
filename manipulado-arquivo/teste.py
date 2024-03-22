with open('teste.txt', 'r+') as arquivo:
    linhas = arquivo.read()
    arquivo.write("\nMais texto")
    for linha in linhas:
        print(linha)
        for caracter in linha:
            print(caracter)
    # print(linhas)