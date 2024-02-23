import requests
# Exemplo 1:
# nome = input("Informe o seu nome: ")
# print(f"Olá, {nome}")


# Exercício 1:
# Ada ingressou no curso superior em Análise e Desenvolvimento
# de Sistemas no ano de 2023.
# Como gosta de planejar seu futuro gostaria de saber em qual
# ano irá concluir seu curso, considerando que irá cursar
# todas as disciplinas disponíveis por semestre e ser aprovada
# em todas elas. Ajude-a desenvolvendo um software:
ano_inicial = 2024
ano_final = ano_inicial + 3
# print(f"Ada iniciou o curso em {ano_inicial} e terminará em {ano_final}")

# Exercício 2:
# Alan, colega de Ada, gostaria de fazer um software para que
# todos (as) os (as) colegas possam identificar em qual ano irão
# concluir seu curso. Você pode ajudá-lo?
# colega = input("Digite o seu nome: ")
# print(f"{colega} iniciou o curso em {ano_inicial} e terminará em {ano_final}")

# Exercício 3:
# Carol irá participar de um congresso na Espanha para apresentar
# os resultados de uma pesquisa sobre viés algorítmico.
# Para isso, ela precisa saber quanto precisa economizar a fim de
# realizar a viagem. Os gastos totais foram orçados em €1.250,00.
# Você pode ajudá-la a descobrir quanto esse valor equivale em
# Reais?
# link = "https://economia.awesomeapi.com.br/last/EUR-BRL"
# req = requests.get(link)
# cotacao = req.json()['EURBRL']['low']
# gastos = 1250 * float(cotacao)
# print(f"Carol gastará R${gastos:.2f}")

# Exercício 3.a:
# Aproveitando que você está desenvolvendo o software para Carol,
# implemente também uma versão que possibilita converter qualquer
# valor de Euros para Reais.
# valor = input("Digite o valor que está orçado em euros para a viagem: ")
# gastos = float(valor) * float(cotacao)
# print(f"O valor que será gasto é R${gastos:.2f}")

# Exercício 4:
# A turma decidiu ir a uma pizzaria após a aula.
# Você poderia fazer um software que calcule:

# Exercício 4.a:
# Quantas pizzas (de 12 pedaços) são necessárias para um número
# de pessoas que come x pedaços cada?
# pessoas = int(input('Quantas pessoas estarão no local: '))
# pedacos = int(input('Quantos pedaços cada pessoa come: '))
# total_pedacos = pessoas * pedacos
# resto = total_pedacos % 12
# pizzas = 0
# if resto > 0:
#     pizzas = int(total_pedacos // 12) + 1
# else:
#     pizzas = total_pedacos // 12
# print(f"Serão necessárias {pizzas} pizzas")

# Exercício 4.b:
# Quantas fatias de pizza (o número de pizzas deve ser informado)
# serão divididas entre x pessoas?
# pizzas = int(input("Quantas pizas serão compradas: "))
# pessoas = int(input("Quantas pessoas estão no local: "))
# pedacos = pizzas / pessoas
# print(f"Cada pessoa poderá comer {pedacos} pedaços")

# Exercício 5:
# Charles está aprendendo a programar e fazendo algumas
# experimentações com código. Você poderia ajudá-lo a
# descobrir como imprimir na tela um texto informado
# ao contrário? Por exemplo, se o usuário digitar “Olá!”,
# o seu inverso é “!ÁlO”.
texto = input("Digite o texto a ser invertido: ")
novo_texto = "".join(reversed(texto))
print(novo_texto)
