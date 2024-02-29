
# Exercício 14: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
# pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
peso_maximo = 50
multa = 0
peso_peixes = float(input('Digite o peso dos seus peixes: '))
peso_excesso = 0
if peso_peixes > peso_maximo:
    peso_excesso = peso_peixes - peso_maximo
    multa = 4 * peso_excesso
    print(f'O valor da multa é de R${multa:.2f}')
else:
    print('Você não tem multa para pagar!')