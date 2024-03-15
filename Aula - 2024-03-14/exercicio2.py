preco = float(input('Insira o preço de um produto: '))
match preco:
    case preco:
        if preco > 50:
            print(f'O produto com imposto é R${preco*1.6:.2f}')
        elif preco <= 50 and preco > 0:
            print('O produto não tem imposto a ser cobrado!')
        else:
            print('Valor inválido!')