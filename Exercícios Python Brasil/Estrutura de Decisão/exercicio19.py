# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
# de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Digite um número maior que 0 e menor que 1000: '))
if numero > 0 and numero < 1000:
    centena = numero // 100
    if centena > 0:
        print(f'{centena} centenas, ')
    numero = numero % 100
    dezena = numero // 10
    if dezena > 0:
        print(f'{dezena} dezenas e ')
    numero = numero % 10
    unidade = numero
    print(f'{unidade} unidades')
else:
    print('Insira um número válido!')