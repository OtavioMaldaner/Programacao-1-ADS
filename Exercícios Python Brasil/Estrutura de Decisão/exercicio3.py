# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
genero = input('Digite uma "F" para Feminino ou "M" para Masculino: ')
if genero.lower() == 'f' or genero.lower() == 'm':
    print('O sexo é válido')
else:
    print("Sexo inválido!")